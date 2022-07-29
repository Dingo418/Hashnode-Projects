## What is Symmetric Encryption? 
Symmetric encryption is a type of encryption that uses a singular key for both decrypting and encrypting text. This is different compared to asymmetric encryption which requires a public and private key. If two entities want to safely communicate via symmetric encryption, they must safely exchange the key. This is easier said than done, and there is a variety of ways to do this. Some examples would be the Diffie–Hellman key exchange or threw Asymmetric encryption. Sadly, this is out of scope for this article.

## Types of Encryption

Symmetric Algorithms fall into two main categories: Block and Stream Ciphers.

### Block Ciphers

Block Ciphers encrypt plaintext by splitting text up into blocks of data (usually 64, 128 or 256 bits). Each of these blocks is processed by several mathematical functions. These blocks can be chained together to provide stronger encryption. Block Ciphers will return a ciphertext that is the same length as the plaintext. If the block of data is smaller than the desired block size, then it will be padded with null data, generally 0's, to reach the desired block size. To decrypt a Block Cipher the inverse functions of the function that encrypted the ciphertext must be used. Block Ciphers are far more secure than Stream Ciphers. They are also far more complicated than Stream Ciphers.

[![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1659097811572/hIFj1WPVN.png align="left")](https://www.tutorialspoint.com/cryptography/block_cipher.htm)
Credit: Tutorialspoint, Block Cipher 


Positives:
- Very Secure
- Reverse engineering is harder
- Easy to make tweaks to the algorithm 

Negatives:
- Relatively Slow
- Longer keys


### Stream Ciphers:

Stream Ciphers encrypt the plaintext one byte at a time. This algorithm supports any key size. The key size greatly affects the security of the encryption. Compared to Block Ciphers, Steam ciphers are relatively simple and fast. Common Stream algorithms used are Salsa20, RC4, CSS and one-time-pads. Most of these encryption methods have been found to have multiple vulnerabilities which render them insecure. This is why you will not see Stream Ciphers used in modern software.

Although Stream Ciphers have a lot of vulnerabilities, they have the mathematically strongest algorithm. It is called a 'one-time pad', where you generate a random key with the same length as the message and only use it **once**. Although, this is impractical and inefficient in general use. 

Positives:
- Fast
- Any size key
- Simple to understand

Negatives:
- Very insecure

Below is an example of a stream cipher using the XOR operation
[![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1658484682323/zB_ouYoj8.png align="left")](https://www.geeksforgeeks.org/difference-between-block-cipher-and-stream-cipher/)
Credit: Geeks for Geeks, Difference between Block Cipher and Stream Cipher

## Stream Cipher Example in Python
Below will be an explanation of the key parts of the code. **This is not a secure implementation of a stream cipher**. This is a simple implementation of a stream cipher. If you want to see a more secure implementation, see [RC4 in Python](https://github.com/manojpandey/rc4).

### **Encryption**
The code below goes through the given variable ```text``` one character at a time. Using the ```ord()``` function we get the integer representation of the letter and the "keyling". The "keyling" is the corresponding character from the key. An easy way to encrypt a character is using the XOR function. This is represented in python by the ```^``` character. The ciphertext would then be converted back into a Unicode character by the ```chr()``` function. This would then be added to the ciphertexts variable. After encrypting the given text, it will write it to ```ciphertext.txt```. This is done as some Unicode characters act weird when copied.
```
def encrypt(text, key):
    ciphertexts = ""
    with open("ciphertext.txt", "w") as f:
        for num,letter in enumerate(text):
            # Acessing 1 byte from the key. It repeats if the key is shorter
            keyling = key[num % len(key)]
            # Uses the XOR operation to encrypt it. ^ is XOR
            ciphertexts += chr(ord(letter) ^ ord(keyling))
        # Has to be written to a file. Clipboard does not work
        f.write(ciphertext)
```
### **Decryption**

Below is the decryption part of the code. It goes through the text file one character at a time. Using the ```ord()``` function we get the integer representation of that letter and the keyling. To reverse the encryption we must know the inverse calculation of XOR. The inverse calculation of an XOR is an XOR. Each character is encrypted with the "keyling" using the XOR function. It is then finally added to the plaintext variable.

```
def decrypt(key):
    plaintext = ""
    with open("ciphertext.txt", "r") as f:
        for num,letter in enumerate(f.read()):
            # Acessing 1 byte from the key. It repeats if the key is shorter then the text
            keyling = key[num % len(key)]
            # The inverse of XOR is XOR. ^ is XOR
            plaintext += chr(ord(letter) ^ ord(keyling))
        return plaintext
```
### **The Full Code**
Below contains a basic user interface to decrypt or encrypt using a Stream Cipher implementation.
```
def decrypt(key):
    plaintext = ""
    with open("ciphertext.txt", "r") as f:
        for num,letter in enumerate(f.read()):
            # Acessing 1 byte from the key. It repeats if the key is shorter
            keyling = key[num % len(key)]
            # The inverse of XOR is XOR. ^ is XOR
            plaintext += chr(ord(letter) ^ ord(keyling))
        return plaintext
def encrypt(text, key):
    ciphertext = ""
    with open("ciphertext.txt", "w") as f:
        for num,letter in enumerate(text):
            # Acessing 1 byte from the key. It repeats if the key is shorter
            keyling = key[num % len(key)]
            # Uses the XOR operation to encrypt it. ^ is XOR
            ciphertexts += chr(ord(letter) ^ ord(keyling))
        # Has to be written to a file. Clipboard does not work
        f.write(ciphertexts)
        

def main():
    while True:
        option = input("Do you want to encrypt or decrypt: ")
        key = input("Please enter your key: ")
        if option == "encrypt":
            text = input("Enter your desired text: ")
            encrypt(text, key)
            print("Your ciphertext is in file ciphertext.txt")
        else:
            print("Your plaintext is: ",decrypt(key))
        
    exit()

if __name__ == "__main__":
    main()
``` 

## Closing Notes
Symmetrical Encryption is a massively complicated topic. Block ciphers are more secure but a lot more complicated. It deserves its own article. The above code can be found [here](https://github.com/Dingo418/Hashnode-Projects/tree/main/Symmetrical%20Encryption) on my Github.

I hope you enjoyed this article about symmetrical encryption. If you have any questions you can always leave a comment below or feel free to reach out to me on Twitter @dingo418.
## Credits:
[Video: Block Cipher Vs Stream Cipher - Cryptography - Cyber Security - CSE4003](https://www.youtube.com/watch?v=XYN5BFZAe1w)
[Cryptology 101: Block Cipher Modes of Operation with Python examplez](https://headfullofciphers.com/2020/12/17/cryptology-101-block-cipher-modes-of-operation)
