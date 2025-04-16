from cryptography.fernet import Fernet
import random
from termcolor import colored

def generate_logo():
    logo = """                                                                                                           


           d8b                                                             
           ?88                                       d8P                   
            88b                                   d888888P                 
  88bd88b   888  d88'  88bd88b?88   d8P ?88,.d88b,  ?88'   d8888b   88bd88b
  88P' ?8b  888bd8P'   88P'  `d88   88  `?88'  ?88  88P   d8P' ?88  88P'  `
 d88   88P d88888b    d88     ?8(  d88    88b  d8P  88b   88b  d88 d88     
d88'   88bd88' `?88b,d88'     `?88P'?8b   888888P'  `?8b  `?8888P'd88'     
                                     )88  88P'                             
                                    ,d8P d88                               
                                 `?888P' ?8P                               


    """
    colors = ['green']
    for line in logo.split("\n"):
        print(colored(line, random.choice(colors)))

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print(colored("Secret key generated and saved as 'secret.key'.", "cyan"))

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)
    print(colored(f"File '{filename}' encrypted and saved as '{filename}.enc'", "green"))

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    output_filename = filename.replace(".enc", "_decrypted.txt")
    with open(output_filename, "wb") as file:
        file.write(decrypted_data)
    print(colored(f"File '{filename}' decrypted and saved as '{output_filename}'", "green"))

def main():
    generate_logo()
    print(colored("Welcome to NKRYPTOR - The Ultimate File Encryption Tool!", "cyan"))
    
    while True:
        print("\n1. Generate Key\n2. Encrypt File\n3. Decrypt File\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            generate_key()
        elif choice == "2":
            filename = input("Enter the file name to encrypt: ")
            key = load_key()
            encrypt_file(filename, key)
        elif choice == "3":
            filename = input("Enter the file name to decrypt: ")
            key = load_key()
            decrypt_file(filename, key)
        elif choice == "4":
            print(colored("Goodbye! Stay Secure!", "magenta"))
            break
        else:
            print(colored("Invalid choice. Please select a valid option.", "red"))

if __name__ == "__main__":
    main()
