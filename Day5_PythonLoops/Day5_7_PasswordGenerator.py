#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pass1 = ""
pass2 = ""
pass3 = ""
for i in range(0,nr_letters):
    letter = letters[random.randint(0,25)]
    # letter = random.choice(letters)
    pass1 += letter
print(pass1)
for j in range(0,nr_symbols):
    symbol = symbols[random.randint(0,9)]
    # symbol = random.choice(symbols)
    pass2 += symbol
print(pass2)
for k in range(0,nr_numbers):
    number = numbers[random.randint(0,10)]
    # number = random.choice(numbers)
    pass3 += number
print(pass3)
easy_pass = pass1 + pass2 + pass3

hard_pass = "".join(random.sample(easy_pass,len(easy_pass)))
print(hard_pass)

length = len(easy_pass)
hard_pass_list = []
for i in range(0,length):
    hard_pass_list.append(easy_pass[i])
print(hard_pass_list)

random.shuffle(hard_pass_list)
password_shuffled = ""
for char in hard_pass_list:
    password_shuffled += char
print(f"your password is : {password_shuffled}")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Error - error when input is all 5.

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P