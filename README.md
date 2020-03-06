# Breached Password Checker

## Requirements
To run this program, Python version 3+ must be installed on your computer and in your executable search path.

## Usage
From an operating system shell, type <code>python pass-check.<code>py</code> password-to-check</code>, where <code>password-to-check</code> is the candidate password.

## Background
Among the measures we take to secure our valuable digital assets, passwords are perhaps the most vulnerable to theft and/or misuse by nefarious actors (what such an actor might refer to as low-hangning fruit). The reasons for this are many&mdash;passwords that are weak and/or easily guessable, passwords written on sticky notes, passwords that are reused across multiple accounts, better hacking tools and massive data breaches (just to name a few).

A password in the wrong hands can obviously result in great personal loss. Consider the consequences of a bad actor gaining access to your checking or savings account, or your 401(k). This thought should make anyone think hard about the quality of the passwords they choose to secure sensitive assets.

One measure of password quality is knowing whether it has ever been leaked in a data breach of the kind we read about with ever increasing frequency (Target, Home Depot, Equifax, LinkedIn, Sony, Yahoo, Facebook, Anthem...should I go on?). Because if a password has been leaked, you can be sure it is in the database of every self-respecting hacker on the planet. And in that case you want to change it immediately (if it is already in use), and in no case ever use it to secure anything because it is <i>burned</i>, <i>dead</i> and <i>useless</i>. Forever.

## Purpose
The program in this repository indicates whether a candidate password (i.e. a password you currently use, or one you are considering using) appears in a <a href=https://haveibeenpwned.com/Passwords target="_blank">publicly available database of passwords</a> that have previously been exposed in a data breach. The objective is to vet a candidate password for its suitability to secure a sensitive resource, such as an email or bank account. Obviously, a password that has been exposed should not be used to secure a sensitive resource, now or ever.

Whether a password has been exposed is just one aspect of its suitability (or quality). For example, just because a password hasn't previously appeared in a data breach does not necessarily mean it is a <i>good</i> password (more on this below). This program is but one test of a password's quality, albeit a crucial one.

If the program indicates a candidate password has previously appeared in a data breach, the password should be considered <i>burned</i> and never again used to secure a sensitive resource. If it is an existing password, then it should be  changed immediately.

The database queried by this program contains more than 500,000,000 (that's 500 million) burned passwords. It is (currently) the largest such database publicly available, and is actively updated every time a data breach exposes more passwords to the public domain.

## Attribution
The ideas and concepts expressed in this software are borrowed entirely from the work of Troy Hunt, whose valuable contributions in the area of password security are documented <a href=https://www.troyhunt.com/tag/pwned-passwords/ target="_blank">here</a>. For a broader view of Troy Hunt's work on security, check out his excellent site <a href=https://haveibeenpwned.com/ target="_blank">Have I Been Pwned</a> (pronounced <i>poned</i>).

## Questions and Concerns
<b>Q</b>: <i>A database of stolen passwords?! Isn't that illegal, or at least highly suspect and/or immoral? What are you up to?</i>

<b>A</b>: The <a href=https://haveibeenpwned.com/Passwords target="_blank">breached-password database</a> used by this program contains passwords that <i>have already been exposed</i> in a data breach; that is, they are now and will forever be in the public domain. More troubling, they are already in the hands of potentially nefarious actors. Passwords in this database should be considered <i>burned</i>, <i>dead</i> and <i>useless</i>, and should therefore never, ever be used again. Indeed the whole point of this database is to allow honest actors to vet the quality of a password they are considering using to secure a sensitive resource. Bottom line: if the candidate password is in the database, don't use it to secure a sensitive resource!

<b>Q</b>: <i>Wait, you want me to type my ultra-secret password into this program, and just trust that you won't steal it?</i>

<b>A</b>: The candidate password supplied to this program is neither transmitted to another computer, nor is it stored anywhere on your computer. If you doubt this claim, feel free to inspect the program's 42 lines of source code to verify it for yourself. If you are not a programmer, and/or you are still skeptical, don't use this program!

<b>Q</b>: <i>How is it possible to look up a password in a online database without transmitting it to another computer?</i>

<b>A</b>: This program leverages a mechanism known as <a href=https://en.wikipedia.org/wiki/K-anonymity target="_blank">k-anonymity</a> to accompish this trick. Specifically, the candidate password supplied to this program is first hashed (using the <a href=https://en.wikipedia.org/wiki/SHA-1 target="_blank">SHA-1</a> algorithm) to a 40-character hexadecimal string. Then the first 5 characters of this hash (not the <i>entire</i> hash) are transmitted to the API fronting the breached-password database. The API responds with a list of all 40-character hashes whose first 5 characters match the given prefix. The program then checks this list for the presence of the candidate password's full 40-character hash. If there is a match, the program reports that the password matching the hash has been breached. Nowhere in this workdflow is a plain-text password trasmitted or stored. The only data that is transmitted are the first 5 characters of a 40-character hash of the candidate password, from which the candidate password could not in any conceivable way be derived. And nothing&mdash;no password, no hash, nothing&mdash;is stored on your computer.

## Caveats
* Absence of evidence is not evidence of absence. That is, if the program reports that a candidate password does not appear in the breached-password database, that does not necessarily mean the password has not been breached. For example, it is possible that the password has been breached, but that this fact is not yet publically known.

* Absence of a candidate password in the breached-password database does not necessarily mean it is a <i>good</i> password. Good passwords should be long, random, and contain a wide variety of character types (not just letters and/or numbers). For tips on creating a good password, have a look <a href=https://www.nist.gov/blogs/taking-measure/easy-ways-build-better-p5w0rd target="_blank">here</a>.

* With regard to the security of the candidate password supplied to this program, as previously explained in the FAQ, the password is neither transmitted to another computer, nor is it stored on your computer. However, in order to use this program you must type the candidate password in clear text on the command line, as an argument to the program&mdash;e.g. <code>python check&ndash;pass.<code>py</code> MySuperSecurePassword</code>. This means, for example, somebody watching over your shoulder might see what you type and steal your password. Therefore, care should be taken when using this program. Even if nobody is watching over your shoulder, make sure to exit the terminal window from which you run the program after you are finished using it.