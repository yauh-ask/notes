**Cross-Site Scripting.**

Types of XSS attacks:

- Stored XSS: code that executes attacker's script is persisted
- Reflected XSS: transient response from server causes script to execute (eg a validation error)
- DOM Based XSS: no server involvement is required (passcode via queryParam)
- Blind XSS: exploits vulnerability in another app (eg log-reader), that attacker can't see or access under normal means




1. How confident are you in the XSS protection of your OSS libraries? (there should be a procedure for resolving security issues: no public issues on GitHub)
2. How carefully do people scrutinize browser plugins? (permissions of these plugins, which could modify the page)
3. If XSS happens, what is your exposure?
4. In your apps, what could a successful XSS attack escalate to? (how hight is the consequences of risk)

XSS Defenses: Never put untrusted data in these places

- directly in a script `<script> <%- userdata %> </script>`
- in a HTML comment `<!--- <%- userdata %> ---->`
- in an attribute name `<iframe <%- userdata %> = "myValue"/>`
- in a tag name `<<%- userdata %> class= "myElm">`
- directly in a <style> block `<style> <%- userdata %> </style>`

XSS Defense: sanitize the data 

example: https://github.com/ESAPI/node-esapi 

careful 'templating JS': `<script> alert("Hello <%- userdata %>") </script>`  => Content-type:'application/json' => keep user's values as values not as code.

XSS Defense: Content Security Policy (CSP)

- Browsers can't tell the difference between scripts downloaded from your origin vs another. It is a single execution content.
- CSP allows us to tell modern browsers which sources they should trust, and for what types of resources.
- This info comes via HTTP response or via header/meta tags  `Content-Security-Policy: script-src 'self' https://mike.works`
- Multiple directives are separated by semicolon / re-defining the directive with the same name has no effect / by default directives are permissive

[List of CSP-directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)

CSP and 'unsafe-inline'
Banning script tags by less JS in HTML as possible: crypto nonces must be generated per pageload and change unpredictably or sha256 (checksum to CSP).

[Helmet to secure Express apps](https://github.com/helmetjs/helmet)


**CSRF or Cross-site request forgery**

To revise

**Clickjacking**

To revise

**Third Party Assets**

1. The people who write dependencies make mistakes, thus:
- reproducible builds, with a lockfile
- use LTS(long-term-support) versions where you care less about bleeding edge features
- support bug bounties in important open source project (Open Collective as a support, filter on issue "security")
- tests that assert only expected requests are sent out (eg, chrome to track url packages)
- subresource integrity attributes (alike to content-security-policy), e.g. adding a hash in a tag `integrity="sha256...` is like a checksum of the contents of this file

2. Vendor Tags:
- these can be updated independently of your deploys
- definitely to avoid adding the scripts which add more scripts
- when "fail secure" is desired, add your own SRI to the script tags
- ask that you vendors VERSION the scripts, so you have control over when nex code lands (and you SRI does not break)
 for js library scanning as a service - https://snyk.io/
 
 
 **HTTPS**
 
 - 2 types of encryption involved: symmetric and Public Key
 -- Public Key is for WRITING messages while Private Key for READING messages
 -- RSA algorithm: product of two huge prime numbers, + exponential math is involved, practical limit on size of message + Private Key can be used to SIGN message
 
 
 *MITM Defense: OpenSSL*
 1. Industry standart library for crypto
 2. Do not implement your own algorithms, protocols or shakes...
 
 There is a range of cli to work with OpenSSL as
 
 - generate a private key `openssl genrsa -aes128 -out my-private.key 2048`
 - generate a public key from a private key `openssl rsa -pubout \ -in my-private.key \ -out my-public.key`
 - make a new certificate signing request `openssl req -new \ key my-private.key \ -out my-request.csr`
 - sign the certificate with your prvate key `openssl x509 -req -days 3 \ -in my-request.csr \ -signkey my-private.key \ -out my-certificate.crt`
 
 
 **HTTPS Downgrading**
 
 To prevent:
 
 - Content-Security-Policy: upgrade-insecure-requests
 - Browser pluggins attempt a "secure upgrade" whenever possible
 
 To prevent based on bad certificate:
 
 - HTTP response header for that: `Strict-Transport-Security: max-age=31536000; includeSubDomains` : includeSubDomains option prevents a broad range of cookie manipulation attacks
 - Add your domain to https://hstspreload.org/ 
