# GitHub: SFhectorj
# Skills Used: Lists, For loops, if statements, range functions, import modules
# Description: This program can be used to generate passwords based on the number of letters, numbers, and
#              symbols you want to use. You can add an extra layer of complexity by having your password shuffled
#              before being printed.

import random
# Here are the variables containing the usable characters for the password.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Interface for the program which takes input for desired amount of characters per type.
print("Password Generator")
letter_input = int(input("Please input the desired length of password:\n"))
number_input = int(input("Please input the amount of numbers to be used in your password:\n"))
symbol_input = int(input("Please input the amount of symbols to be used in your password:\n"))
complexity_choice = input("Would you like an additional layer of complexity for your password?: Yes or No\n")
complexity_choice.lower()

# We store the password in this variable as a string.
final_password = ""

# For loops using range funtion for each character type.
for letter in range(1, letter_input + 1):
    # Use the random function from the random module to generate random character.
    random_letter = random.choice(letters)
    # Adds the generated character to the final_password variable.
    final_password += random_letter

for number in range(1, number_input + 1):
    random_number = random.choice(numbers)
    final_password += random_number

for symbol in range(1, symbol_input + 1):
    random_symbol = random.choice(symbols)
    final_password += random_symbol

# If statement based on input from user.
if complexity_choice == "yes":
    # For more complex passwords the order is completely shuffled using the shuffle function.
    # The characters are added into a list to keep compatibility with shuffle function.
    complex_list = list(final_password)
    random.shuffle(complex_list)
    # Characters are converted back to a string using the join function.
    final_complex = ''.join(complex_list)
    print(f"Generated Password:\n {final_complex}")
else:
    print(f"Generated Password:\n {final_password}")
