# print higher and lower logo
from art import logo
from art import vs


# method to make first two guess selections

from game_data import data
import random


def make_random_choice(datas):
    choice = random.choice(datas)
    return choice

# ask who has more followers as input
# method to compare guess1 with guess 2

def compare(choice1, choice2, userchoice):
    if userchoice == "A" and choice1["follower_count"] > choice2["follower_count"]:
        print("you're right")
        return True
    elif userchoice == "B" and choice2["follower_count"] > choice1["follower_count"]:
        print("you're right")
        return True
    else:
        # print("Sorry that's wrong, Game Over!!")
        return False


def update_choices(input1, input2):
    new_choice1 = input2
    new_choice2 = make_random_choice(data)
    return new_choice1, new_choice2


choice1 = make_random_choice(data)
choice2 = make_random_choice(data)
# print(choice1)
# print(choice2)

score = 0
continue_game = True
while continue_game:
    if score != 0:
        print(f"Your're right! Current score : {score}")
    # print guess 1
    print(logo)
    # print("compare A : " + choice1["name"] + " " + str(choice1["follower_count"]))
    print("compare A : " + choice1["name"] + " a " + choice1["description"] + ", from " + choice1["country"])
    print(vs)
    # print("compare B : " + choice2["name"] + " " + str(choice2["follower_count"]))
    print("compare B : " + choice2["name"] + " a " + choice2["description"] + ", from " + choice2["country"])
    # print vs symbol

    userinput = input("Who has more followers, Type 'A' or 'B' : ").upper()
    # print(userinput)
    correct_compare = compare(choice1, choice2, userinput)
    # update method guess1 with guess2 if they are right
    if not correct_compare:
        continue_game = False
        print(f"Sorry that's wrong, Your final score : {score}")
# continue the process till the user makes incorrect guess
    if continue_game:
        score += 1
        print("current score: " + str(score))
        new_choice1, new_choice2 = update_choices(choice1, choice2)
        choice1 = new_choice1
        choice2 = new_choice2
        print(f"{choice1}\n" + f"{choice2}")







