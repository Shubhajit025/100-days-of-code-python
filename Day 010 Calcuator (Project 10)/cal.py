from art import logo
print(logo)

# Addition 👇
def add(n1, n2):
    """Addition between two numbers."""
    return n1 + n2

# Subtraction 👇
def subtract(n1, n2):
    """Subtraction between two numbers."""
    return n1 - n2

# Multiplication 👇
def multiply(n1, n2):
    """Multiplication between two numbers."""
    return n1 * n2

# Division 👇
def divide(n1, n2):
    """Division between two numbers."""
    return n1 / n2


cal_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


calculator = True

while calculator:

    re_cal = True
    f_number = float(input("Type the first number : "))
    while re_cal:

        for operator in cal_dict:
            print(operator)
        choice_operators = input("Type a mathematical operators to operate, choose one. : ")
        s_number = float(input("Type the second number : "))
        result = cal_dict[choice_operators](f_number, s_number)
        print(f"{f_number} {choice_operators} {s_number} = {result}")
        with_or_without = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation : ").lower()

        if with_or_without == "y":
            re_cal = True
            f_number = result
        elif with_or_without == "n":
            re_cal = False
            print("\n" * 10)
            again = input("Type 'y' to start new calculation or 'q' to quit: ").lower()

            if again == "q":
                calculator = False
                print("Calculator closed 👋. Thank you.")
            elif again == "y":
                calculator = True
