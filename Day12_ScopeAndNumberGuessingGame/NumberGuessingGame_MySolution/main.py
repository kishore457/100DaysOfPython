from logo import game_logo
from random import randint
print(game_logo)
number_to_guess = randint(1,100)
print(f"Welcome to number guessing game!\n I'm thinking of a number between 1 and 100.\n Psst, the correct answer is {number_to_guess}")
guesses = 0
level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
if level == "easy":
    guesses = 10
elif level == "hard":
    guesses = 5


def make_a_guess():
    guess = int(input("Make a guess: "))
    return guess




while guesses > 0:
    guessed_number = make_a_guess()
    if guessed_number > number_to_guess:
        print("Too high\n guess again")
    elif guessed_number < number_to_guess:
        print("Too low\n guess again")
    elif guessed_number == number_to_guess:
        print("you guessed right you won!!")
        break
    guesses -= 1

    if guesses > 0:
        print(f"you have {guesses} attempts remaining to guess the number.")
    elif guesses == 0:
        print("Game over!!, you ran out of guesses")
