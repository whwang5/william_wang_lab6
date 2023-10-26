def encode_password(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

decoded_pswrd = []
decoded_str_pswrd = ''

def decode(encoded_pswrd):
    decode_key = {
        -3: 7,
        -2: 8,
        -1: 9,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        1: 1,
        2: 2,
        0: 0
    }

    global decoded_str_pswrd
    for i in range(8):
        decoded_pswrd.append(decode_key[(int(encoded_pswrd[i]) - 3)])
        decoded_digit = str(decoded_pswrd[i])
        decoded_str_pswrd = decoded_str_pswrd + decoded_digit
    return decoded_str_pswrd


while True:
    print("Menu")
    print("-------------")
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
        print(decode(encoded_password))


    elif choice == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
