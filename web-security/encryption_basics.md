Types of encryption #
There are two main types of encryption:

1. Symmetric Encryption #
In symmetric encryption, the same key is used for both encryption and decryption. Here’s a good analogy to explain how symmetric encryption works:

Suppose John needs to send a message to Carl. John will put a message in a box and will lock the box. Carl already has a duplicate copy of the key which was used to lock the box. Carl will receive the box and will unlock it using the key. This is symmetric encryption. The symmetric encryption is much faster than asymmetric encryption and is used to encrypt a large amount of data.

The disadvantage of this encryption type is that the sender and receiver will have to send their key to each other. An attacker may access this key while in transit and will be able to read all the messages. The keys used in symmetric encryption are not very large, as the max length is 256 bits.

2. Asymmetric Encryption #
In asymmetric encryption, the sender and receiver use a separate key to encrypt and decrypt the message. This is also known as PKI (Public Key Infrastructure). The advantage of this encryption is that the keys are not transferred over the network. So, it is much safer than asymmetric encryption. This encryption is achieved through a public-private key model.

The recipient sends a public key to all the senders. The senders then encrypt the messages using this public key. When the receiver receives the message, it uses its private key to decrypt the message. The keys used in asymmetric encryption are fairly large and can be around 2048 bits.

Since the asymmetric encryption is very slow, it is normally used once to exchange the encryption key safely. After that, all the communication is done using symmetric encryption.

What is an encryption algorithm? #
An encryption algorithm is a mathematical formula used to transform data into ciphertext. An encryption algorithm uses an encryption key to transform plaintext into ciphertext. The ciphertext can be changed back to plaintext using a decryption algorithm and the decryption key.

Below are some of the commonly used encryption algorithms:

AES
DES
Blowfish
TwoFish
RC4, RC5, RC6
What is a brute force attack? #
In a brute force attack, an attacker tries to guess the decryption key. The attacker is not required to do this manually, and there is computer software that performs the same actions. To prevent this from happening, the key should be very strong, so that it becomes impossible for the computer to try all the combinations.

Let’s see what we mean by a strong key. We know that data is represented by bits in computing language. Each bit can have a value of 0 or 1. If a key is 2 bits long then there are four possible combinations, i.e. 00, 01, 10, 11. This is very easy for computers to crack.

Let’s take a key which is 256 bits long. The total number of possible combinations are 2^{256}2
​256
​​ . A 256-bit private key will have 115, 792, 089, 237, 316, 195, 423, 570, 985, 008, 687, 907, 853, 269, 984, 665, 640, 564, 039, 457, 584, 007, 913, 129, 639, 936 possible combinations. No supercomputer can crack that in any reasonable timeframe. So, to prevent brute force attacks, the key should be of sufficient length.
