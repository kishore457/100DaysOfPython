print("welcome to treasure island")

input1 = input("Welcome to treasure island's first step, which direction you want to go left or right? : ").lower()
if(input1 == "left"):
    print("Hmm, you have good luck, you can continue :)")
    input2 = input("We are at Wonder Land, do you want to swim or go boating?").lower()
    if (input2 == "boating"):
        print("welcome aboard, lets go to the secret Treasure Town")
        input3 = input(
            "congrats, You are in treasure town, the treasure is in Red room. Choose any room from red, blue or yellow").lower()
        if (input3 == "yellow"):
            print("congrats you are the winner!! Treasure is yours")
        elif (input3 == "blue"):
            print("You choose a great fall, game over!!")
        elif (input3 == "red"):
            print("You got burnt in fire, game over!!")
    else:
        print("You can swim along the tide to a great fall, game over!!")
else:
    print("Hmm, you are right into witches house, Game Over :0 ")