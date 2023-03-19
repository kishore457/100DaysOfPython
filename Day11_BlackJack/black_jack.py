from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

computer_total = 0
player_total =0
def add_cards(card):
    global player_total
    global computer_total
    chosen_card = random.choice(cards)
    card.append(chosen_card)
    print(f"new added card : {card}")
    if card == player_cards:
        player_total += chosen_card
        print(f"{card} : {player_total}")
        if player_total > 21:
            print(f"player total is {player_total}, you loose")
    elif card == computer_cards:
        computer_total += chosen_card
        print(f"{card} : {computer_total}")



        # global statement below
    # if card == player_cards:
    #     global player_total
    #     player_total += chosen_card
    #     if player_total > 21:
    #         print(f"total is {player_total}, you loose")
    #     else:
    #         print(f"player_total : {player_total}")

def play():
    global player_total
    global computer_total
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        print(logo)
        for i in range(2):
            player_cards.append(random.choice(cards))
        for j in player_cards:
            player_total += j
        for i in range(2):
            computer_cards.append(random.choice(cards))
        for j in computer_cards:
            computer_total += j
        print(f"players cards : {player_cards}")
        print(f"player_total : {player_total}")
        print("computer first cards : " + str(computer_cards[0]))
        # print(f"computer_total : {computer_total}")
        while_continue = True
        while while_continue:
            is_continue = input("Type 'y' to get another card, type 'n' to pass:")
            if is_continue == 'y':
                add_cards(player_cards)
            elif is_continue == 'n':
                print(f"Player Total : {player_total}, Computer Total : {computer_total}")
                if player_total > 21:
                    print("you loose")
                elif computer_total > 21:
                    print("You win!")
                elif player_total <22 and computer_total <22:
                    if player_total < computer_total:
                        print("you lost")
                    elif computer_total < 16:
                        add_cards(computer_cards)
                    elif player_total > computer_total:
                        print("You won")
                while_continue = False
                # if player_total > computer_total and player_total < 22 and computer_total < 22:
                #     print(f"player total : {player_total}, computer total : {computer_total}, you Win!!")
                # if player_total > computer_total and computer_total < 15:
                #     add_cards(computer_cards)
                #     print(f"player total : {player_total}, computer total : {computer_total}, you Win!!")
                # elif (computer_total > 21):
                #     print("you win!!")
                # elif (computer_total < 22):
                #     print("you lose!!")

    elif play == 'n':
        print("Sorry to hear, see you again :)")
        play()
play()







