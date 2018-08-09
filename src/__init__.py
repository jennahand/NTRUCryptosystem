

# FUNCTIONS
from src.NTRU import encrypt, decrypt


def display_title_bar():

    print("\t***********************************************")
    print("\t********  NTRU PUBLIC KEY CRYPTOSYSTEM ********")
    print("\t***********************************************")


def get_input_file_name():
    print("Please enter the full name of the file for input (with extension) at the prompt below")
    # Raw_input is used to collect data from the user
    file = input()
    print(type(file))
    return file


def get_output_file_name():
    print("Please enter the full name of the file for output (with extension) at the prompt below")
    # Raw_input is used to collect data from the user
    file = input()
    return file


def decrypt_file(file):
    print("Please enter the full name of the file for output (with extension) at the prompt below")
    # Raw_input is used to collect data from the user
    file = input()
    ciphertext = open(file, "rb").read()
    plaintext = decrypt(ciphertext)
    output_file = open("plaintext.txt", "w+")
    for byte in plaintext:
        output_file.write(chr(byte))


def encrypt_file():
    print("Please enter the full name of the file for input (with extension) at the prompt below")
    # Raw_input is used to collect data from the user
    file = input()
    plaintext = open(file, "rb").read()
    cipher_text = encrypt(plaintext)
    output_file = open("ciphertext.txt", "w+")
    for byte in cipher_text:
        output_file.write(chr(byte))


# MAIN PROGRAM


# choice = ''
# while choice != 'q':
#     display_title_bar()
#
#     # Let users know what they can do.
#     print("\n[1] Encrypt a file.")
#     print("[2] Decrypt a file.")
#     print("[q] Quit.")
#
#     choice = input("What would you like to do? ")
#
#     # Respond to the user's choice.
#     if choice == '1':
#         encrypt_file()
#     elif choice == '2':
#         decrypt_file()
#     elif choice == 'q':
#         print("\nExiting.")
#     else:
#         print("\nChoose a valid menu item.\n")
