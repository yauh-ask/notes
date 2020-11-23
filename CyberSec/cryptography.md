Definitions

Code - a system that substitutes one word or phrase for another; intended to prvide secrecy or/and efficiency, e.g. "10" Code System used by Police

Cipher - a system that uses mathematical algorithms to encrypt and decrypt messages, types are stream cipher (operates on one charachter or bit of a message at atime), 
block cipher (operates on large segments of the message at the same time). Examples: substitution ciphers ABC -> XYZ (change the characters in a message),
transposition ciphers ABC -> CAB (rearrange the charachters in a message, decryption key is needed)

Crypthographic Math

Exclusive Or (XOR): true when exactly one of two inputs values is true.

PseudoRandom to generate random numbers.

Confusion: every bit of the ciphertext must depend upon more than one bit of encryption key.

Diffusion: changing a single bit of the plain text should change about 50% of the ciphertext bits.

Obfuscation: uses cryptography to hide source code from users.

The perfect encryption algorithm is one-time pad encryption.

The cryptographic lifecycle: initiation (CIA), development and acqusition, implementation and assessment, operations and maintanence, sunset(destroy/archive sensitive material).
On integrity: the corectness of cryptographic keys and other critical security parameters must be preserved. Authentification, authorization, and non-repudation (Alice would like to be able
to prove to Charlie that a message she received actually came from Bob) should be supported.

MODERN ENCRYPTION ALGORITHMS

DES - Data Encryption Standart
- symmetric encryption algorithm
- block cipher operating on 64-bit blocks
- key lenght of 56 bits
- now considered insecure

3DES - same as above with 3 keys, effective key lenght 112 bits, phased out as above
 
 1) keying option
 - K1 != K2 != K3

2) keying option
- K1 = K3

3) All 3 keys are the same


RIJNDAEL or AES, Advanced Encryption Standart (command: aescrypt -e -p Pasword -o outputfile.aes fileToEncrypt.txt)

- symmetric encryption algorithm
- block cipher operating on 128-bit blocks
- key length of 128, 192, or 256 bits
- considered secure

BLOWFISH

- public domain algorithm
- designed as a DES replacement
- uses Feitsel network
- combines substitution and transposition
- key length from 32 to 448 bits
- not secured

TWOFISH
- symmetric encryption algorithm
- block cipher operating on 128-bit blocks
- key length of 128, 192, or 256 bits
- considered secure

RC4: network encryption on Wired Equivalent Privacy (WEP), Wi-Fi Protected Access (WPA), SSL/TSL; uses pseudorandom keystream, yet insecure, uses a selected range of encryption keys.


