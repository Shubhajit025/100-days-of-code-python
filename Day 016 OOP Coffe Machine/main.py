from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:

    item = menu.get_items()
    choice = input(f"What you like to drink? ({item}): ").lower()

    if choice == "off":
        print("Coffee Machine Turned Off.")
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        coffee = menu.find_drink(choice)
        if money_machine.make_payment(coffee.cost):
            if coffee_maker.is_resource_sufficient(coffee):
                coffee_maker.make_coffee(coffee)

