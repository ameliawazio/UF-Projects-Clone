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

    # This will make you get out from the program
    elif choice == "3":
        break
