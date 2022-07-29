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