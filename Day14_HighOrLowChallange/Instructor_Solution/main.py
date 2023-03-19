from art import logo, vs
from game_data import data
import random

# display art
print(logo)
score = 0

def format_data(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """take the users guess and followers counts and returns if they got it right."""
    if a_followers > b_followers:
        # if guess == "a":
        #     return True
        # else:
        #     return False
        return guess == "a"
    else:
        return guess == "b"


game_should_continue = True
account_b = random.choice(data)
# make the game repeatable
while game_should_continue:
    # generate a random account from the game

    # making account at postion B become the next account at position b.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")
    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
    # check if user is correct



    ## Get follower count of each account

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ## use if statement to check if user is correct

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right Current score : {score}.")
    else:
        print(f"Sorry, that's wrong. Final Score : {score}.")
        game_should_continue = False
    # score keeping





# clear the screen
