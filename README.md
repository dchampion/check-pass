# Breached Passwork Checker

## Summary
This program indicates whether a candidate password appears in a database of passwords that have previously been exposed in a data breach. The objective is to vet a candidate password for suitability in securing a sensitive resource, such as an email or bank account. Obviously, a password that has been exposed should not be used to secure a sensitive resource, now or ever.

Whether a password has been exposed is just one aspect of its quality. For example, just because a password hasn't previously appeared in a data breach does not necessarily mean it is a <i>good</i> password (more on this below). This program is but one test of a password's quality.

If the program indicates a candidate password has previously appeared in a data breach, the password should be considered <i>burned</i> and never again used to secure a sensitive resource. Should this be an existing password, then it should be  changed immediately.

The breached-password database used by this program (currently) contains some 500-billion entries. It is (currently) the largest such database publically available, and is actively updated every time a data breach exposes more such passwords to the public domain.

The concepts contained in this program are borrowed entirely from the work of Troy Hunt, whose valuable contributions in the area of password security are documented <a href=https://www.troyhunt.com/tag/pwned-passwords/>here</a>.

## FAQ
<b>Q</b>: <i>A database of stolen passwords?! Isn't that illegal, or at least highly suspect and immoral? What are you up to?</i>

<b>A</b>: The breached-password database used by this program contains passwords that <i>have already been exposed</i> in a data breach; that is, they are now and will forever be in the public domain. More troubling, they are already in the hands of potentially nefarious actors. Passwords in this database should be considered <i>burned</i>, <i>dead</i> and <i>useless</i>, and should therefore never, ever be used again. Indeed the whole point of this database is to allow honest actors to vet the quality of a password they are considering using to secure a sensitive resource. Bottom line: if the candidate password is in the database, don't use it.

<b>Q</b>: <i>Wait, you want me to type my ultra-secret password into this program, and just trust that you won't steal it?</i>

<b>A</b>: The candidate password supplied to this program is neither transmitted to another computer, nor is it stored anywhere on your computer. If you doubt this claim, feel free to inspect the program's 42 lines of source code to verify it for yourself. If you are not a programmer, and/or you are still skeptical, don't use this program!

<b>Q:</b>: <i>How is it possible to look up a password in a online database without transmitting it to another computer?</i>

<b>A</b>: This program leverages a mechanism known as <a href=https://en.wikipedia.org/wiki/K-anonymity>k-anonymity</a> to accompish this trick. Specifically, the candidate password supplied to this program is first hashed (using the <a href=https://en.wikipedia.org/wiki/SHA-1>SHA-1</a> algorithm) to a 40-character hexadecimal string. Then the first 5 characters of that hash (not the <i>entire</i> hash) are transmitted to the API fronting the breached-password database. The API responds with a list of all 40-character hashes whose first 5 characters match the prefix supplied. The program then checks this list for the presence of the candidate password's full 40-character hash. If there is a match, the program reports the password has been breached. Nowhere in this workdflow is a password trasmitted or stored. The only data that is transmitted are the first 5 characters of a 40-character hash of a password, from which a candidate password could not in any conceivable way be derived. And nothing&mdash;no password, no hash, nothing&mdash;is stored on your computer.

## Caveats
* Absence of evidence is not evidence of absence. That is, if the program reports that a candidate password does not appear in the breached-password database, that does not necessarily mean the password has not been breached. For example, it is possible that the password has been breached, but that this fact is not yet publically known.

* Absence of a candidate password in the breached-password database does not necessarily mean it is a <i>good</i> password. Good passwords should be long, random, and contain a wide variety of character types (not just letters and/or numbers). For tips on creating a good password, have a look <a href=https://www.nist.gov/blogs/taking-measure/easy-ways-build-better-p5w0rd>here</a>.

* With regard to the security of the candidate password supplied to this program, as previously explained in the FAQ, the password is neither transmitted to another computer, nor is it stored on your computer. However, in order to use this program you must type the candidate password in clear text on the command line, as an argument to the program&mdash;e.g. <code>python check&ndash;pass.<code>py</code> MySuperSecurePassword</code>. This means, for example, somebody watching over your shoulder might see what you type and steal your password. Therefore, care should be taken when using this program. Even if nobody is watching over your shoulder, make sure to exit the terminal window from which you run the program after you are finished using it.