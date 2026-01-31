print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
upside_down = input("You are at the end of a road. Chose where you want to go."
                    "Type \"left\" or \"right\"\n").lower()
if upside_down == "right":
    print("You fell into a whole. Game Over.")
elif upside_down == "left":
    the_gate = input("You have come to a lake. There is an island middle of the lake."
          "Type \"wait\" to wait for a boat, or type \"swim\" to swim across.\n").lower()
    if the_gate == "swim":
        print("A Shark attacked you, when you are swimming. You died. Game Over.")
    elif the_gate == "wait":
        vecna = input("You arrived at the island unharmed. There is a house of three doors."
                      "one red, one yellow and one blue. Which colour do you choose?\n").lower()
        if vecna == "red":
            print("You entered in a room full of fire. You died. Game over.")
        elif vecna == "yellow":
            print("You found the treasure! You Win!")
        elif vecna == "blue":
            print("You entered a room full of beasts. You died. Game over.")
        else:
            print("You typed wrong. Start again.")
    else:
        print("You typed wrong. Start again.")
else:
    print("You typed wrong. Start again.")
