MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte" : {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
        "water_resource": 500,
        "milk_resource": 500,
        "coffee_resource": 100,
        "money_resource": 100,
    }

def get_resources(resource):
    resources = resource
    return resources

print(type(MENU["espresso"]["ingredients"]["water"]))

def check_resources(coffeetype):

    if MENU[coffeetype]["ingredients"]["water"] <= resources["water_resource"]:
        if MENU[coffeetype]["ingredients"]["coffee"] <= resources["coffee_resource"]:
            if coffeetype != "espresso":
                if MENU[coffeetype]["ingredients"]["milk"] <= resources["milk_resource"]:
                    return True
                else:
                    print("Sorry, we doesn't have enough milk, Required :" + str(MENU[coffeetype]["ingredients"]["milk"]) + ", Available: " + str(resources["milk_resource"]))
                    return False
            else:
                print("Your order is available")
                return True
        else:
            print("Sorry, we doesn't have enough coffee, Required :" + str(MENU[coffeetype]["ingredients"]["coffee"]) + ", Available: " + str(resources["coffee_resource"]))
            return False
    else:
        print("Sorry, we doesn't have enough water, Required :" + str(MENU[coffeetype]["ingredients"]["water"]) + ", Available: " + str(resources["water_resource"]))
        return False
#

    # if MENU[coffeetype]["ingredients"]["water"] > resources["water_resource"]:
    #     print("Sorry not enough water")
    #     return False
    # elif coffeetype != "espresso":
    #     if MENU[coffeetype]["ingredients"]["milk"] > resources["milk_resource"]:
    #         print("Sorry not enough milk")
    #         return False
    # elif MENU[coffeetype]["ingredients"]["coffee"] > resources["coffee_resource"]:
    #     print("Sorry not enough coffee")
    #     return False
    # else:
    #     return True
def process_coins():
    print("Please insert coins")
    quarter = int(input("How many quarters: "))
    dime = int(input("How many dimes: "))
    nickle = int(input("How many nickles: "))
    penny = int(input("How many pennies: "))
    total_change = quarter*0.25 + dime*0.1 + nickle*0.05 + penny*0.01
    print(f"Your total change : ${total_change}")
    return total_change

def do_transaction(cash, coffeedrink):
    if cash >= MENU[coffeedrink]["cost"]:
        returned_change = round(cash - MENU[coffeedrink]["cost"],2)
        print(f"Your change : ${returned_change}")
        return returned_change

def update_resources(coffeedrink):
    resources["water_resource"] = resources["water_resource"] - MENU[coffeedrink]["ingredients"]["water"]
    resources["coffee_resource"] = resources["coffee_resource"] - MENU[coffeedrink]["ingredients"]["coffee"]
    if coffeedrink != "espresso":
        resources["milk_resource"] = resources["milk_resource"] - MENU[coffeedrink]["ingredients"]["milk"]
        print(f"New Resources : milk : "+str(resources["milk_resource"])+", water :"+str(resources["water_resource"])+", coffee : "+str(resources["coffee_resource"]))
    if coffeedrink == "espresso":
        print(f"New Resources : water :"+str(resources["water_resource"])+", coffee : "+str(resources["coffee_resource"]))


continue_buying = True



while continue_buying:
    user_input = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    print(user_input)

    if user_input == "off":
        print("machine turning off..")
        continue_buying = False
    elif user_input == "report":
        print(get_resources(resources))
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if check_resources(user_input):
            if do_transaction(process_coins(), user_input):
                update_resources(user_input)
                print(f"Enjoy your {user_input}")
            else:
                print("not enough change. Refunded")
        else:
            print("Not enough resources.")