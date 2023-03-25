from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine_object = MoneyMachine()
coffeemaker_object = CoffeeMaker()
menu_object = Menu()

turnon = True
while turnon:
    options = menu_object.get_items()
    choice = str(input(f"What would you like? {options}"))
    print(choice)
    if choice == 'off':
        print("Turning off coffee machine..")
        turnon = False
    elif choice == 'report':
        coffeemaker_object.report()
        moneymachine_object.report()
    else:
        if coffeemaker_object.is_resource_sufficient(menu_object.find_drink(choice)):
            # moneymachine_object.money_received = moneymachine_object.process_coins()
            if moneymachine_object.make_payment(menu_object.find_drink(choice).cost):
                coffeemaker_object.make_coffee(menu_object.find_drink(choice))
                print(coffeemaker_object.resources)




