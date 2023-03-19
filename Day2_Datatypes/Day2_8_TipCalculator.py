print("welcome to the tip calculator :) $$")

total_bill = float(input("What was the total bill?"))
percent_tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
total_people = float(input("How many people to split the bill?"))
eachperson_tip = (total_bill*percent_tip/100)/5
print(eachperson_tip)
eachperson_total = total_bill/5 + eachperson_tip
print(eachperson_total)
eachperson_total_round = "{:.2f}".format(eachperson_total)
print(f"Each person should pay : ${eachperson_total_round}")
