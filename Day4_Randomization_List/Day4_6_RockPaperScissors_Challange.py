# Rock - 🗿
# paper - 📄
# scissors - ✂

# Rules :
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
import random

options = ["🗿","📄","✂"]

user_choice = int(input("choose 0 for rock, 1 for paper and 2 for scissors."))
user_selection = options[int(user_choice)]
if user_choice == 0:
    print(f"you selected Rock: {user_selection}")
elif user_choice ==1:
    print(f"you seleected Paper: {user_selection}")
else:
    print(f"you selected scissors : {user_selection}")

computer_choice = random.randint(0,2)
computer_selection = options[int(computer_choice)]
if computer_choice == 0:
    print(f"computer chose Rock: {computer_selection}")
elif computer_choice ==1:
    print(f"computer chose Paper: {computer_selection}")
else:
    print(f"computer chose scissors : {computer_selection}")

# logic
if user_choice == 0 and computer_choice == 0:
    print("both of you chose Rock its a draw!")
elif user_choice == 1 and computer_choice == 1:
    print("both of you chose Paper its a draw!")
elif user_choice == 2 and computer_choice ==2:
    print("both of you chose Scissors its a draw!")
elif user_choice == 0 and computer_choice ==1:
    print("user chose rock and computer chose paper: computer won!!,")
elif user_choice == 0 and computer_choice == 2:
    print("user chose Rock and computer chose scissors : You won!!")
elif user_choice == 1 and computer_choice == 0:
    print("user chose paper and computer chose rock: You won!!")
elif user_choice == 1 and computer_choice == 2:
    print("user chose paper and computer chose scissors: computer won!!")
elif user_choice == 2 and computer_choice == 0:
    print("user chose scissors and computer chose rock: computer won!!")
elif user_choice == 2 and computer_choice == 1:
    print("user chose scissors and computer chose paper: you won!!")



