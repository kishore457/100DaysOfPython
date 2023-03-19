# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
fullname = name1+name2
true_count = fullname.lower().count("t") + fullname.lower().count("r") + fullname.lower().count("u") + fullname.lower().count("e")

love_count = fullname.lower().count("l") + fullname.lower().count("o") + fullname.lower().count("v") + fullname.lower().count("e")

total_count = str(true_count) + str(love_count)

total_count_int = int(total_count)

if total_count_int <10 or total_count_int >90:
    print(f"Your score is {total_count_int}, you go together like coke and mentos.")
elif total_count_int > 40 and total_count_int < 50:
    print(f"Your score is {total_count_int}, you are alright together.")
else:
    print(f"Your score is {total_count_int}.")
