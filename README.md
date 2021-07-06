# Breached Password Checker
## Summary
Indicates whether a password has been leaked in a publicly-known data breach.

## Requirements
To run this program, Python 3+ must be installed on your computer.

To check if Python is installed on your computer, and if so to verify you have version 3 or greater, open a terminal window (e.g. <code>cmd</code> in Windows, <code>bash</code> in Linux, or <code>Terminal</code> in MacOS) and type <code>python --version</code>. If the version displayed is less than 3, or you receive an error, download and install the latest Python version <a href=https://www.python.org/downloads target="_blank">here</a></i>.

## Installation
Use one of the following methods to install the leaked password checker on your computer:
* If Git is installed, navigate to a clean directory on your file system and type <code>git clone https<nolink>://github.com/dchampion/check-pass.git</code>. This will install the program into a subdirectory called <code>check-pass</code>.

* If <code>Git</code> is not installed, or you do not wish to use it, click the <code>Code</code> button on this page and select <code>Download ZIP</code> to download and extract a zipped version of the program into a clean file system directory.

## Set Up a Virtual Environment
To avoid polluting your global Python environment with the dependencies required by this program, set up and activate a virtual environment. Execute all of the following commands from a command-line prompt in the directory into which you cloned/installed the program.

* Install your virtual environment:

    * If using <code>Windows</code> (cmd) or <code>Linux</code> (bash), type <code>python -m venv .venv</code>

    * If using <code>MacOS</code> (Terminal), type <code>python3 -m venv .venv</code>

* Activate your virtual environment:

    * If using <code>Windows</code> (cmd), type <code>".venv/Scripts/activate.bat"</code> (you must include the double-quotes for this command to work).

    * If using <code>Linux</code> (bash) or <code>MacOS</code> (Terminal), type <code>source .venv/bin/activate</code> (note on some systems the path may be <code>.venv/Scripts/activate</code>).

* Install the program dependencies into your virtual environment:

    * Type <code>pip install -r requirements.txt</code>

With the successful completion of these three steps, you should be ready to run the leaked password checker.

## Usage
From an operating system shell, type <code>python check_pass.py candidate</code>, where <code>candidate</code> is the password to test for exposure in a data breach.

# Background
Among the measures we take to secure our digital assets, passwords are perhaps the most vulnerable to theft and misuse by bad actors; what a hacker might refer to as low-hangning fruit. The reasons for this are many&mdash;passwords are often weak or easily guessable,  written on Post-It notes, reused across multiple accounts and/or exposed in massive data breaches.

A password in the wrong hands can result in great personal loss. Consider the consequences of a bad actor gaining access to your checking or savings account, or your 401(k). This thought should cause anyone to think hard about the quality of the passwords they choose to secure sensitive assets.

One crucial but overlooked measure of password quality is knowing whether it has previously been leaked in a data breach. Massive data breaches perpetrated by malicious hackers are occuring with ever greater frequency (see Target, Home Depot, Equifax, LinkedIn, Sony, Yahoo, Facebook and Anthem, to name a few). If a password has been leaked it is effectively useless; it will be among the first to be tried if a hacker attempts to break into your account. In that case you want to change it immediately, and never use it again to secure anything of value.

## Purpose
The program in this repository determines whether a candidate password (i.e. a password you currently use, or one you are considering using) appears in a <a href=https://haveibeenpwned.com/Passwords target="_blank">publicly available database of passwords</a> that have previously been exposed in a data breach. The objective is to vet a candidate password for its suitability to secure a sensitive resource, such as an email or bank account. A password that has been exposed should not be used to secure a sensitive resource, now or ever.

Whether a password has been exposed is just one aspect of its suitability. For example, just because a password hasn't previously appeared in a data breach does not necessarily mean it is a <i>good</i> password (more on this below). This program is but one test of a password's quality, albeit a crucial one.

If the program indicates a password has previously appeared in a data breach, the password should be considered <i>burned</i> and never again used to secure a sensitive resource. If it is an existing password, then it should be changed immediately.

The database queried by this program contains more than 500,000,000 (that's 500 million) leaked passwords. It is (currently) the largest such database publicly available, and is actively updated every time a data breach exposes more passwords to the public domain.

## Attribution
The ideas and concepts expressed in this software are borrowed entirely from the work of Troy Hunt, whose valuable contributions in the area of password security are documented <a href=https://www.troyhunt.com/tag/pwned-passwords/ target="_blank">here</a>. For a broader view of Troy Hunt's work on security, check out his excellent site <a href=https://haveibeenpwned.com/ target="_blank">Have I Been Pwned</a> (pronounced <i>poned</i>).

## Questions and Concerns
<b>Q</b>: <i>A database of stolen passwords?! Isn't that illegal, or at least highly suspect and/or immoral? What are you up to?</i>

<b>A</b>: The <a href=https://haveibeenpwned.com/Passwords target="_blank">leaked-password database</a> used by this program contains passwords (more precisely <i>hashed</i> passwords) that <i>have already been exposed</i> in a data breach; that is, they are now and will forever be in the public domain. More troubling, they are already in the password lists of potentially nefarious actors. Passwords in this database should be considered <i>burned</i>, <i>dead</i> and <i>useless</i>, and should therefore never, ever be used again. Indeed the whole point of this database is to allow honest actors to vet the quality of a password they are considering using to secure a sensitive resource. Bottom line: if the candidate password is in the database, don't use it to secure a sensitive resource!

<b>Q</b>: <i>Wait, you want me to type my ultra-secret password into this program, and just trust that you won't steal it?</i>

<b>A</b>: The candidate password supplied to this program is neither transmitted to, nor is it stored on, any computer (local or remote). If you doubt this claim, feel free to inspect the program's 42 lines of source code to verify it for yourself. If you are not a programmer, and/or you are still skeptical, don't use this program!

<b>Q</b>: <i>How is it possible to look up a password in a online database without transmitting it to another computer?</i>

<b>A</b>: This program leverages a mechanism known as <a href=https://en.wikipedia.org/wiki/K-anonymity target="_blank">k-anonymity</a> to protect a candidate password from being exposed. Specifically, the candidate password is hashed (using the <a href=https://en.wikipedia.org/wiki/SHA-1 target="_blank">SHA-1</a> algorithm) to a 40-character hexadecimal string, just the first 5 characters of which (not the <i>entire</i> hash) are transmitted to the API fronting the leaked-password database. The API sends back a list of all 40-character hashes (actually just the 35-character suffixes, since we already know the prefix) whose first 5 characters match the given prefix. The program then checks this list&mdash;locally, in its own memory space&mdash;for the presence of the candidate password's full 40-character hash. If there is a match, the program reports that the password matching the hash has been leaked. Nowhere in this workflow is a plain-text password trasmitted or stored. The only data that is transmitted are the first 5 characters of a 40-character hash of the candidate password (<i>from</i> the program <i>to</i> the API), from which a candidate password could not in any conceivable way be derived, and a list of potential matches (<i>to</i> the program <i>from</i> the API). And nothing&mdash;no password, no hash, nothing&mdash;is logged, printed or stored on any computer.

<b>Q</b>: <i>Even if I transmit only part of my hashed password, and receive a list of potential matches in return, doesn't this significantly reduce the keyspace required for a determined hacker to derive the candidate password?</i>

<b>A</b>: This concern is addressed in two ways. First, all traffic between the client (this program) and the API is <a href=https://en.wikipedia.org/wiki/Transport_Layer_Security _target="blank">TLS-encrypted</a>; that is, it is secured by the same time-tested, battle-hardened HTTPS protocol used to protect sensitive communications of the type we engage in regularly on the world-wide web; for example when we submit payment information to an online store to pay for products or services. This means that even if the request and/or response is intercepted by a bad actor, its contents&mdash;nameley the 5-character hash prefix in the request, and/or the list of 35-character hash suffixes in the respone&mdash;will be forever invisible to the interceptor. Second, the API provides an optional feature known as <a href=https://www.troyhunt.com/enhancing-pwned-passwords-privacy-with-padding/ _target="blank">cryptographic padding</a>, which this program uses, and which is a means of threat mitigation that should put even the super-paranoid at ease.

## Caveats
* With regard to the security of the candidate password supplied to this program, as previously explained in the <i>Questions and Concerns</i> section above, the password is neither transmitted to nor stored on any computer. However, before it can be hashed and truncated into an innocuous string of characters, the candidate password must be typed in clear text as an argument to the program on the command line&mdash;e.g. <code>python check_pass.py MySuperSecurePassword</code>. This means, for example, somebody watching over your shoulder might see what you type and steal your password. Therefore, care should be taken when using this program. Even if nobody is watching over your shoulder, make sure to exit the terminal window from which you run the program after you are finished using it.

* In spite of the great pains taken by the API provider to protect the confidentiality of its consumers (not just flea-sized ones like me, but big companies whose very existence depends on effective security, like <a href=https://www.identityautomation.com/ _target="blank">Identity Automation</a>, <a href=https://1password.com/ _target="blank">1Password</a> and even the <a href=https://www.mozilla.org/ _target="blank">Firefox</a> web browser), it must be disclaimed that no system is unhackable. Even in the extremely unlikely event the provider were hacked (say by a state-level actor), the best that hacker could do is steal a hash fragment. With this information a very determined hacker <i>might</i>, through some combination of brute force, ingenuity and luck, be able to derive a password, but the probability of this is vanishinly small.

* Absence of evidence is not evidence of absence. That is, if the program reports that a candidate password does not appear in the leaked-password database, that does not necessarily mean the password has not been leaked. For example, it is possible that the password has been leaked, but that this fact is not yet publicly known.

* Absence of a candidate password in the leaked-password database does not necessarily mean it is a <i>good</i> password. Good passwords should be long and random. For tips on creating a good password, have a look <a href=https://www.nist.gov/blogs/taking-measure/easy-ways-build-better-p5w0rd target="_blank">here</a>.