import random
import Day4_1_myModule_Randomization

# random whole number
random_int = random.randint(1,10)
print(random_int)

# random float number
random_float = random.random()
print(random_float)

#random float from 1 to 5
random_number = random.randint(1,5)+ random.random()
print("{:.2f}".format(random_number))
print(random_number)


print(Day4_1_myModule_Randomization.pi)