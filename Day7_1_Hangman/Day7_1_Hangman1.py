#step 1
import random

word_list = ["ardvark", "baboon", "camel"]

#Todo 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = word_list[random.randint(0,len(word_list)-1)]
print(f"Chosen word : {chosen_word} ")
#Todo 2 - As the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter : ").lower()

#Todo 3 - Check if the letter the user guessed is one of the letters in the chosen_word.
for i in chosen_word:
    if i == guess:
        print("true")
    else:
        print("false")

