Asymmentric cryptography is based upon the difficulty of solving complex math problems, e.g. factoring large prime numbers.

RSA
- asymmentric encryption algorithm
- variable length key from 1024 to 4096 bits
- considered secure

Pretty Good Privacy (PGP)
*by Phil Zimmerman
- open PGP (GnuPG), command `gpg --gen-key`, it relies on other encryption algorithms (sym or assym, or both).
Randomly generated key is actually used to encrypt the contents of a message when using PGP.

ECC (Eliptic Curve Cryptography): no factorization, but a discrete log probleme.
QUANTUM COMPUTING to develop in cryptography.

TOR protocol
- facilitates an anonymous internet
The Onion Router is a software package that uses encryption and relay nodes to facilitate anonymous internet access.
- based on Perfect Forward Secrecy (hides node's identity from each other)


Cryptographic Applications

TLS depends upon pairing of encryption and hash functions known as cipher suites. Session keys are known as ephemeral keys. SSL was a predecessor of TLS.

Information Rights Management (IRM): enforcing data rights, provisioning access, implementing access controls models. One of the important tools to build up IRM
programme is Digital Rights Management (DRM), it provides the ownders of intellectual property with the tecnical means to prevent the unauthorized use of their content
through the use of encryption technology, e.g. fairplay in music industry. Business Aplication of DRM:

- protect trade secrets and other intellectual property
- limit redistribution of information
- revoke access after expiration data

Special cases as smatrcard-readers are examples of low-power cryptography; networked cryptography requires low latency; homomorphic encryption (the same results after
computation on ecrypted text as after plaintext).

Blockchain
Distributed, immutable ledger
