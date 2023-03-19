from art import logo



import random
# step4
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

#step 6 and 8
def calculate_score(cards):
    # verify if any got blackjack
    if sum(cards) == 21 and len(cards)==2:
        return 0

    # check for an 11(ace). If the score is already over 21 remove the 11 and replace it with a 1. you might use append() and remove()
    if 11 in cards and sum(cards) < 21:
        cards.remove(11)
        cards.append(1)

    # return sum
    return sum(cards)
# step 13
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "lose, opponent has blackjack"
    elif user_score == 0:
        return "You win, you have blackjack"
    elif computer_score > 21:
        return "Opponent went over. you win!!"
    elif user_score > 21:
        return "You lose"
    elif user_score > computer_score:
        return " you win!"
    else:
        return "You lose"



def play_game():

    print(logo)
    # step 5
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # step 10
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards : {user_cards}, current score : {user_score}")
        print(f"computer card : {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get anothe card type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # step 11 and 12 - computer while loop
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score == calculate_score(computer_cards)

    # step 14
    print(f"your final cards : {user_cards}, final score : {user_score}")
    print(f"computer final cards : {computer_cards}, final score : {computer_cards}")
    # step 13
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack Type 'y' or 'n'") == 'y':
    play_game()


