def encode_password(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode_password(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

while True:cd
    print("Menu\n-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        if len(password) != 8 or not password.isdigit():
            print("Invalid password format. Please enter an 8-digit password containing only integers.")
        else:
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")

    elif choice == "2":
        if 'encoded_password' in locals():
            decoded_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        else:
            print("No encoded password available. Please encode a password first.")

    elif choice == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
