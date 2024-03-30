# Brendan's 1st Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")

# input determines how many of each character type in randomly generated password
nr_letters= int(input(f"\nHow many letters would you like in your password?\n")) 
nr_symbols = int(input(f"\nHow many symbols would you like?\n"))
nr_numbers = int(input(f"\nHow many numbers would you like?\n"))

# EASY MODE (V1) - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

list_of_letters = []
list_of_symbols = []
list_of_numbers = []

# create a list of the random letters to be printed
for characters in range(0, nr_letters):
    list_of_letters.append(letters[random.randint(0, len(letters) - 1)])

# create a list of the random symbols to be printed
for characters in range(0, nr_symbols):
    list_of_symbols.append(symbols[random.randint(0, len(symbols) - 1)])

# create a list of the random numbers to be printed
for characters in range(0, nr_numbers):
    list_of_numbers.append(numbers[random.randint(0, len(numbers) - 1)])

fixed_order_password = "".join(list_of_letters + list_of_symbols + list_of_numbers)

# print(f"\nYour randomly generated password is: {fixed_order_password}")

# CHALLENGE MODE (V2) - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# creating a fixed order list so I can randomize it later
fixed_order_list = list_of_letters + list_of_symbols + list_of_numbers

# randomizing list to create an actual random list!!
random.shuffle(fixed_order_list)

# creating "true random password" variable (assigned to previously shuffled list)
true_random_list = fixed_order_list

# converting list to string; true random password creation.
random_order_password = "".join(true_random_list)

print(f"\nYour randomly generated password is: {random_order_password}")

