# Najib Mosquera
# Amelia Wazio

# Function to encode values
def encode(password):
    encoded_password = ""
    for digit in password:
        enc_digit = str((int(digit) + 3) % 10)
        encoded_password += enc_digit
    return encoded_password

# def decode(): '''will be here'''
# Amelia Wazio
def decode(password):# Decoding function for Najib Mosquera

    enc_string = ''
    password = str(password)
    for num in password:
        num = int(num)
        password = int(password)
        if num >= 3:
            enc_num = (num - 3)
            enc_num = str(enc_num)
            enc_string += enc_num
        else:
            enc_num = ((num + 10) - 3) # For numbers that would be negative
            enc_num = str(enc_num)
            enc_string += enc_num
    return enc_string

# Menu in function for easier recall
def menu():
    print('''Menu
-----------
1. Encode
2. Decode
3. Exit'''
    )

encoder_decoder = True


# Entering the program, letting user choose option.
while encoder_decoder:
    menu()
    print()
    choice = input("Please enter an option:")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = encode(password)
        print("Your password has been encoded and stored!\n")
    #elif choice == "2":
        #print(f'The encode password is {encoded_password}')
    # Amelia Wazio added option 2
    elif choice == "2":
        password = input('Please enter your password to encode: ')
        decode(password)
        print(f'The encoded password is {password}, and the original password is {enc_string}.')

    # This will make you get out from the program
    elif choice == "3":
        break
