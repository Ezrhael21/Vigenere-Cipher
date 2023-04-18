# Ezrhael R. Sicat
# BSCpE 1-5
# 04/05/2023
# Program 3 - The Vigenere Cipher

# Ask the user for the message
while True:
    user_text = input("Input your message: ")
    if user_text.isupper() and ' ' not in user_text:
        break
    else:
        print ("Invalid Input. Please Enter an uppercase letter without spaces.")

# Ask the user for key
while True:
    user_key = input("Input your key: ")
    if user_key.isupper() and ' ' not in user_key:
        break
    else:
        print("Invalid input. Please enter an uppercase letter without spaces.")

# Create a list of letters
import string
letter_list = list(string.ascii_uppercase)

# Create a list of numbers from 0 to 25
number_list = list(range(0,26))

# Convert the length of the key to the same length of the message
key = (user_key[:len(user_text)] * ((len(user_text) // len(user_key[:len(user_text)])) + 1))[:len(user_text)]

# Encrypt the user text to its corresponding number
encrypted_user_text = []
for i in user_text:
    index = letter_list.index(i)
    encrypted_user_text.append(number_list[index])

# Encrypt the user key to its corresponding number
encrypted_user_key = []
for i in key:
    index = letter_list.index(i)
    encrypted_user_key.append(number_list[index])

# Add the numbers of the message and the key
# Modify the numbers into the list
# Convert the modified number to its corresponding letter
# Print Output