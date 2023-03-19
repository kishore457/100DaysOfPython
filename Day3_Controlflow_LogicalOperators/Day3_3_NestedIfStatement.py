print("welcome to roller coster ticker center")

height = int(input("what is your height in cm : "))
if height > 120:
    print("Enjoy the ride")
    age = int(input("Enter your age :"))
    if age <12:
        print("please pay 5$")
    elif age <= 18:
        print("please pay 7$")
    else:
        print("please pay 12$")
else:
    print("Sorry we can't give you ticket because you are short")