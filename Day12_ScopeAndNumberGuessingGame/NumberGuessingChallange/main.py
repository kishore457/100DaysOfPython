from logo import logo
import random
print(logo)
choices_count = 0
number_to_guess = random.randint(1,100)
print(f"the number to guess is : {number_to_guess}")
game_level = input("what level do you want to play? Easy or Hard : ").lower()
if game_level == "easy":
    choices_count = 10
elif game_level == "hard":
    choices_count = 5

while choices_count >0:
    guessed_number = int(input("Enter your number : "))
    if guessed_number == number_to_guess:
        print(f"You win!! You guessed the number: {guessed_number}")
        break
    elif guessed_number != number_to_guess:
        if guessed_number > number_to_guess:
            print("too high")
        elif guessed_number < number_to_guess:
            print("too low")
        print(f"your guessed number is wrong")
        choices_count -= 1
        print(f"Remaining guesses : {choices_count}")
        if choices_count == 0:
            print("Game over :(")



