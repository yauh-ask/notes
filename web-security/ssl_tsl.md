SSL certificates validation level #
Before a Certification Authority (CA) issues an SSL certificate to an organization, they have to validate the organization. The CA needs to validate that the organization is doing legal business and owns the domain. This is what’s known as SSL certificate validation.

There are three main types of validations:

1. Domain Validation Certificates #
Domain Validation SSL or DV SSL is the most basic type of SSL certificate. This type of certificate can be obtained in a few minutes and is not very expensive. This certificate is suitable for websites that just need encryption and nothing more.

To obtain this certificate, an applicant needs to prove their control over the domain name only. The issued certificate contains the domain name that was supplied to the certification authority within the certificate request.

2. Organization Validation Certificates #
To acquire this certificate, the applicant needs to prove that their company is a registered and legally accountable business. Getting this certificate may take 3-4 days, as the business is vetted to confirm that it is a legal business. This type of certificate is suitable for sites that need the user to authenticate.

The OV SSL provides a way for customers to check the verified business information in the certificate details section. This is not available in Domain Validation Certificates.

3. Extended Validation Certificates #
This certificate is very expensive and takes some time, as a lot of vetting is done before this certificate is issued. This is suitable for applications that ask for confidential details of users like credit card numbers.

This certificate can be easily distinguished from the other two certificates, as the URLs of websites with this certificate have a green address bar containing the company name.

Types of SSL certificates #
The SSL certificates can be divided into three types based on the number of domains it protects.

1. Single-name SSL certificates #
A single-name SSL certificate can only be used on a single domain or IP. It is not applicable on sub domains. For example, if www.mysite.com has a certificate then it is not applicable to blog.mysite.com.

This is the default SSL certificate type and it is available at all validation levels.

2. Wildcard SSL certificates #
A wildcard SSL certificate is applicable to a domain and all its subdomains. For example, if *.mysite.com has a wildcard certificate then this certificate will be applicable on all its sub-domains like contact.mysite.com or mail.mysite.com will also have the certificate.

3. Multi-Domain SSL Certificates #
A multi-domain SSL certificate lists multiple distinct domains on one certificate. With an MDC, domains that are not subdomains of each other can share a certificate. For example, domains like www.mysite.com, www.example.com, and www.abc.com can share the same certificate.

