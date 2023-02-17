#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

for letter in range(0 , nr_letters + 1):
  random_int_letters = random.randint(1 , len(letters)) - 1
  password.append(letters[random_int_letters])

for symbol in range(0 , nr_symbols + 1):
  random_int_symbols = random.randint(1 , len(symbols)) - 1
  password.append(symbols[random_int_symbols])

for number in range(0 , nr_numbers + 1):
  random_int_numbers = random.randint(1 , len(numbers)) - 1
  password.append(numbers[random_int_numbers])

random.shuffle(password)
result = ''.join(password)
print(result)