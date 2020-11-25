Confidentiality, integrity and availability, known as the CIA triad, is a guideline for information security for an organization. 
Confidentiality ensures the privacy of data by restricting access through authentication encryption. Integrity assures that the information 
is accurate and trustworthy. Availability ensures that the information is accessible to authorized people.

Confidentiality

Another term for confidentiality would be privacy. Company policies should restrict access to the information to authorized personnel and ensure that 
only those authorized individuals view this data. The data may be compartmentalized according to the security or sensitivity level of the information. 
For example, a Java program developer should not have to access to the personal information of all employees. Furthermore, employees should receive training 
to understand the best practices in safeguarding sensitive information to protect themselves and the company from attacks. Methods to ensure confidentiality 
include data encryption, username ID and password, two factor authentication, and minimizing exposure of sensitive information.

Integrity

Integrity is accuracy, consistency, and trustworthiness of the data during its entire life cycle. Data must be unaltered during transit and not changed 
by unauthorized entities. File permissions and user access control can prevent unauthorized access. Version control can be used to prevent accidental changes 
by authorized users. Backups must be available to restore any corrupted data, and checksum hashing can be used to verify integrity of the data during transfer.

A checksum is used to verify the integrity of files, or strings of characters, after they have been transferred from one device to another across your local 
network or the Internet. Checksums are calculated with hash functions. Some of the common checksums are MD5, SHA-1, SHA-256, and SHA-512. A hash function uses a 
mathematical algorithm to transform the data into fixed-length value that represents the data, as shown in Figure 2. The hashed value is simply there for comparison.
From the hashed value, the original data cannot be retrieved directly. For example, if you forgot your password, your password cannot be recovered from the hashed
value. The password must be reset.

After a file is downloaded, you can verify its integrity by verifying the hash values from the source with the one you generated using any hash calculator.
By comparing the hash values, you can ensure that the file has not been tampered with or corrupted during the transfer.

Availability

Maintaining equipment, performing hardware repairs, keeping operating systems and software up to date, and creating backups ensure the availability of
the network and data to the authorized users. Plans should be in place to recover quickly from natural or man-made disasters. Security equipment or software, 
such as firewalls, guard against downtime due to attacks such as denial of service (DoS). Denial of service occurs when an attacker attempts to overwhelm resources
so the services are not available to the users.
