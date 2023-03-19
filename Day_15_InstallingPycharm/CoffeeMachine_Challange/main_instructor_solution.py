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

profit = 0

resources = {
    "water" : 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
#     comparing the resources with menu to check if there are sufficient ingredients.
#     is_enough = True
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"sorry there is not enough {item}.")
#             is_enough = False
#     return is_enough

    # comparing the resources with menu to check if there are sufficient ingredients.
    """returns true is resources are available and false if not available"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How man quarters? : ")) * 0.25
    total += int(input("How man dimes? : ")) * 0.10
    total += int(input("How man nickles? : ")) * 0.05
    total += int(input("How man pennies? : ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or
    False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change : ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    choice = input("what would you like ? (espresso, latte, cappuccino) : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']} ml")
        print(f"Milk : {resources['milk']} ml")
        print(f"Coffee :{resources['coffee']} g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


