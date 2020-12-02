What is CSRF? #
Cross-site Request Forgery (CSRF), is an attack that tricks a web browser into executing an unwanted action in an application after a user logs in. It allows an attacker to force a logged-in user to act without their consent or knowledge.

In a CSRF attack, the attacker cannot access the data because the attacker does not have access to the response. This can be devastating, as the attacker can force the user to transfer funds from a banking website or share sensitive information.

How does CSRF work? #
To perform a CSRF attack, a few conditions should be met.

Cookie-based session handling – The user has already logged in into the website that is being attacked, and the website relies on cookies to identify the user.

No unpredictable request parameters – The requests that perform the malicious action do not contain any parameters whose values the attacker cannot determine or guess. For example, when tricking a user into transfering funds, the attacker must not be required to know the password of the user.

CSRF attack using a GET request #
Let’s look at an example of a CSRF attack using a GET request. Suppose a user, Alex, is a customer of ABC bank. He is logged into the bank website. This means the session is currently active, and login information is maintained in the cookies.

Now, suppose a request to transfer funds looks like this:

GET http://abcbank.com/transfer.do?acct=Bob&amount=$500 HTTP/1.1
The attacker will create a request in which the account details of the attacker will be provided.

GET http://abcbank.com/transfer.do?acct=attacker&amount=$500 HTTP/1.1
The attacker has created the request. The only thing they need to do now is trick the user into sending this request from their own browser.

The attacker can create a promotional email which it will send to the user. This email will contain a hyperlink as shown below:

<a href="http://abcbank.com/transfer.do?acct=attackerA&amount=$500">Get the offer!</a>
If the user clicks on the hyperlink then the transaction will go through and money will be transferred to the attacker’s account.

As you can see, the user must already be logged in for this attack to be successful. Otherwise, the user will get a login prompt and become skeptical of the link.

CSRF attack using POST request #
In an ideal scenario, the GET request is not used for state changes. Normally the state change operations are done through a POST request.

In the case of POST, the user’s browser sends parameters and values in the request body and not the URL, as in the case of a GET request.

Therefore, tricking the user to operate a POST request is a bit difficult. With a GET request, the attacker only needs the victim to send a URL with all the necessary information. In the case of POST, a request body must be appended to the request.

The attacker can create a website and add a JavaScript code to it. They will then send the link of this website to the user through a phishing email.

When the user clicks on the email, the malicious website will send a POST request to the bank application.

`<body onload="document.csrf.submit()">
 
<form action="http://abcbank.com/transfer" method="POST" name="csrf">
    <input type="hidden" name="amount" value="500">
    <input type="hidden" name="account" value="attacker">
</form>`

As soon as this page loads, the hidden form will be submitted, which will, in turn, send the POST request.

Methods to prevent CSRF attacks. #
1. Using CSRF tokens #
This is also known as an anti-CSRF token or synchronizer token. An anti-CSRF token is a type of server-side CSRF protection. It is a random string that is only known to the user’s browser and the web application. This is how it works:

When a request is sent to a web server, it generates a token and stores it.
The token is statically set as a hidden field of the form.
When the form is submitted by the user the token is included in the POST request data.
The application compares the token generated and stored by the application with the token sent in the request.
If these tokens match, the request is valid. Otherwise, the request is considered invalid and is rejected.
Now even if an attacker creates a malicious POST request, it is not possible to add the token as the attacker would not be aware of it.

2. Same site cookies #
The SameSite flag in cookies is a relatively new method of preventing CSRF attacks and improving web application security. As we see in the method above, an attacker creates a different website that sends a POST request when the user clicks on it through a phishing attack.

If the session cookie is marked as a SameSite cookie, it is only sent along with requests that originate from the same domain. Therefore, even if the user clicks on the hyperlink provided by the attacker, the cookies will not be sent.

Best practices to avoid a CSRF attack #
There are few things that a user can keep in mind to save itself from a CSRF attack.

Always log out of the website once work is complete. This will close the session and remove cookies.

Try not to use multiple websites at the same time. If you are logged in into a website in one browser tab and using a malicious website in another tab, then the chances of CSRF attack increase.

Do not allow browsers to remember passwords.


