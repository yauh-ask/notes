In asymmetric cryptography:
1) Users do not need to share their private keys
2) Users can and should share their public keys
3) Evesdropping protection is not needed during key exchange
4) We still need to prevent imposters: how do we know that the person who sends the key is the one we need/trust?

Trust Models

- personal knowledge
- web of trust (WOT): indirect trust relationships, participants digitally sign the public keys of people they know personally; decentrilized, high entry req.
- public key infrastructure (PKI): based on WOT, yet centralized via CA, which provides a digital certificate containing public key.

Hash Functions

One-way function that transform a variable length input into unique fixed-length output. Charachteristics:
- one-way function can not be reversed
- the output of a hash function will always be the same length, regardless of the input size
- no two inputs to a hash function should produce the same output
They fail if they are revrsible, or not collision resistant.

Message Digest 5 (MD5), 128-bits hashes and _message digest_ is another term for _hash_; MD5 is no longer secure.
SHA-1, SHA-2, SHA-3 (by NIST) ; alternative to them is RIPEMD.

Application of hash is HMAC (hash-based message authentification code): combines symmetric cryptography and hashing, provides authentication and integrity,
create and verify message authentication code by using secret key in conjuction with a hash function. Another application in combo with asym cryptography is
digital certificates and signatures.

Digital Signatures depends upon
1) Collision Resistant hash functions
2) Asymmetric cryptography


Signed message Recipient knows
- the owner of the public key is the person who signed the message, aka authentication
- the message was not altered after being signed, aka integrity
- the recipient can prove these facts to a third party, non-repudation

! Digitally signing messages does not provide confidentiality (encryption on top is necessary then).

Digital Signature Standart, its approves algorithms:
- digital signature algorithms (DSA)
- RSA
- Elliptic Curve Digital Signature Algorithm (ECDSA)






