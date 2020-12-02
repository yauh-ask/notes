What is a Cross-site Scripting attack? #
The Cross-site Scripting attack, also known as XSS attack, is a kind of attack in which a malicious script is added to a website. When a user accesses this website then they accidentally run this malicious script, compromising their data as the attacker gets control of the user’s browser.

Types of Cross-site Scripting Attack #
The XSS attack can be categorized into two types:

1. Stored Cross-site Scripting Attack #
This is the most dangerous type of XSS attack because it is very easy for the attacker to inject a malicious script through this method. These attack targets websites that allow user input and store it in the database, e.g. comments.

The attacker writes the malicious script inside the input box, for example, a comment box. When the attacker clicks submit, the malicious script is saved as a comment in the website database. When a user opens this website, the malicious script runs on the browser as soon as the comments load.

The malicious script can attack the user through the following methods:

Installing browser-based Keyloggers to capture keystrokes of the victim. This can be dangerous as the attacker might use this to get access to social media passwords, email passwords, credit card info, banking passwords, etc.

Capturing session cookies of the user, which can be used to trigger some other kind of attack, like a CSRF attack.

Redirecting users to other malicious websites.

2. Reflected Cross-site Scripting Attack #
In this kind of attack, the attacker tricks the user into clicking a link that contains the malicious script. This kind of attack is a bit more difficult to execute than stored XSS.

The user may receive the malicious link through email, search results, or advertisements on another website. As soon as the user clicks on the link, the malicious script is executed on the user’s browser. This script can then steal browser data, such as cookies, and send it to the attacker.

How to prevent XSS #
Since XSS works by injecting malicious code into a website, the website owners should make sure that all user inputs are validated before they are stored into the database. The theory here is to treat all data or input as malicious until they pass certain criteria, like type and length requirements.

Sanitizing user input is another mitigation method that essentially requires all user data to be cleaned of potentially dangerous symbols that are usually used in HTML markup and JavaScript code. There are lots of tools available that blacklist HTML tags in user input. If your website allows HTML in user input then you can use these tools to blacklist the tags that build malicious code.

