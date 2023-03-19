print("welcome to roller coster ticket center")

height = int(input("what is your height in cm ?:"))
age = int(input("what is your age?"))
bill = 0
if height >= 120:
    print("you are eligible to buy tickets")
    if age < 12:
        bill = 5
        print("charge : $5")
    elif age <= 18:
        bill = 7
        print("charge : $7")
    else:
        bill = 12
        print("charge : $12")
    want_photo = input("do you want a photo : Type y or n")
    if want_photo == 'y':
        bill += 3
    print(f"total bill is ${bill}")
else:
    print("sorry you are not eligible to buy tickets")
