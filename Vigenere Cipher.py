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
# Create a list of numbers from 0 to 25
# Convert the length of the key to the same length of the message
# Encrypt the user text to its corresponding number
# Encrypt the user key to its corresponding number
# Add the numbers of the message and the key
# Modify the numbers into the list
# Convert the modified number to its corresponding letter
# Print Output