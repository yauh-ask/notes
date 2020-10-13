Cross-Site Scripting.

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
