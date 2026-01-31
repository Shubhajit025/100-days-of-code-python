from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

earnings = 0

print(logo)

# TODO 3 : If user typed report, show ingredients status of coffee machine
def report():
    """Inform about the current ingredients status of coffee machine to user."""
    if ask == "report":
        resources_water = resources["water"]
        resources_milk = resources["milk"]
        resources_coffee = resources["coffee"]
        status = f"'Water' = {resources_water}ml\n'Milk' = {resources_milk}ml\n'Coffee' = {resources_coffee}gm\n'Money' = ${earnings}"
        print(status)

# TODO 4 : Check is there enough resources to make a coffee to serve customer 👇.
def resource_check(coffee_type):
    """Checking resources, so that the machine can make a coffee or not."""
    coffee_maker = MENU[coffee_type]["ingredients"]

    for item in coffee_maker:
        if resources[item] < coffee_maker[item]:
            print(f"Sorry, Not enough {item}.")
            return False

    return True

# TODO 5 : Process all the coins as per value and store the total value 👇.
def process_coins():
    """Asking user to deposit coins first to get a coffee and shows total value."""
    total_value = 0

    print("Please deposit coins first.")

    try: # For an edge case. If we give any input except numbers it gives an error, Value error. To overcome this using try, except.
        quarter = float(input("How many quarters?: ")) * 0.25
        dime = float(input("How many dimes?: ")) * 0.10
        nickel = float(input("How many nickels>: ")) * 0.05
        penny = float(input("How many pennies?: ")) * 0.01

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return 0

    total_value += (quarter + dime + nickel + penny)
    return total_value

# TODO 6 : Check is the transaction successful, or failed 👇.
def transaction(deposit_value, coffee_type):
    """Checking, is the coffee price matched with the deposited value of user.
    If matched give user a coffe and change if needed, else
    return the money and inform user that insufficient balance."""

    cost = MENU[coffee_type]["cost"]

    if deposit_value < cost:
        print("Sorry, Not enough balance. Money refunded.")
        return None

    left_change_value = round((deposit_value - cost), 2)
    if left_change_value > 0:
        print(f"Kindly receive your change ${left_change_value}.")

    return cost

# TODO 7 : Make the coffe the user or customer choose. Make sure transaction should complete, there is enough resources or ingredients 👇.
def processing_coffee(coffee_type):
    """If transaction successful,
    and there is enough ingredients to make the drink,
    start make coffee and also deduct ingredients and should serve the coffee as per coffee type."""

    global earnings

    needed_ingredients = MENU[coffee_type]["ingredients"]

    for item in needed_ingredients:
        resources[item] -= needed_ingredients[item]

    earnings += MENU[coffee_type]["cost"]
    print(f"Here is your {coffee_type}, Enjoy!")

# TODO 8 : Make a Start point which can also break the loop by bool value 👇.
coffee_machine_is_on = True

# TODO 9 : Make the coffee Machine Ongoing till it is shut down or turned off by some one 👇.
while coffee_machine_is_on:

    # TODO 1 : Ask user what type of coffee he/she wants 👇.
    ask = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2 : Turn off the Coffee Machine by entering 👇.
    if ask == "off":
        print("Coffe Machine Shutting Down.")
        coffee_machine_is_on = False

    # TODO 3 : If user typed report, show ingredients status of coffee machine, implemented here 👇.
    elif ask == "report":
        report()

    elif ask in MENU:
        # TODO 4 : Check is there enough resources to make a coffee to serve customer, implemented here 👇.
        if resource_check(ask):

            # TODO 5 : Process all the coins as per value and store the total value, implemented here 👇.
            customer_deposition_amount = process_coins()

            # TODO 6 : Check is the transaction successful, or failed, implemented here 👇.
            paid = transaction(customer_deposition_amount, ask)

            if paid:
                # TODO 7 : Make the coffe the user or customer choose. Make sure transaction should complete, there is enough resources or ingredients, implemented here 👇.
                processing_coffee(ask)

    else:
        print("Invalid choice taken. Choose a valid one please.")
