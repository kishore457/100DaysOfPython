
import random
# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_members = len(names)-1
random_number = random.randint(0,total_members)
print(f"{names[random_number]} is going to buy the meal today!")

print(random.choice(["kishore","williamson","jackson"]))