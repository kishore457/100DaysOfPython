# choosing a random number between 1 and 100
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
answer = randint(1, 100)
print("welcome to number guessing game!\nI'm thinking of a number between 1 and 100.")
print(f"Psst, the correct answer is {answer}")
# function to check user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too Low")
    else:
        print(f"You got it! The answer was {answer}")
# Make function to set difficulty
def set_difficulty():
    level = input("choose a difficulty. Type \"easy\" or \"hard\" ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
# let the user guess a number.
turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number")

while
guess = int(input("Make a guess : "))
check_answer(guess, answer)
# track the number of turns and reduce the number by  1 if they get it wrong
# repeat the guessing functionality if they get it wrong
