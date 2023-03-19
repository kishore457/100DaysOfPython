from random import randint
# global constants
EASY_LEVEL_TRUNS = 10
HARD_LEVEL_TURNS = 5
# generate random number
answer = int(randint(1, 100))
print("welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")




# function to compare the guessed number and actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("too high")
    elif guess < answer:
        print("too low")
    else:
        print(f"you won!!, you guessed the number : {answer}")

def set_difficutly():
    level = input("choose a difficulty easy or hard : ")
    if level == "easy":
        return EASY_LEVEL_TRUNS
    elif level == "hard":
        return HARD_LEVEL_TURNS

# let customer guess the number
guess = int(input("Make a guess : "))






