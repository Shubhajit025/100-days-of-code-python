print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_or_not = input("Would you like to give some tip? Type yes for \"Yes\" or type no for \"No\".").lower()

if tip_or_not == "yes":
    tip = int(input("What percentage tip would you like to give? 10 12 15 "))
    people = int(input("How many people to split the bill? "))
    tip_percentage = (bill * (tip / 100))
    total_bill_with_tip = (bill + tip_percentage)
    final_bill_with_tip = round((total_bill_with_tip / people),2)
    print(f"Each person should pay : ${final_bill_with_tip}")
elif tip_or_not == "no":
    people = int(input("How many people to split the bill? "))
    final_bill_without_tip = round(bill / people , 2)
    print(f"Each person should pay : ${final_bill_without_tip}")
else:
    print("You typed an invalid input.")
