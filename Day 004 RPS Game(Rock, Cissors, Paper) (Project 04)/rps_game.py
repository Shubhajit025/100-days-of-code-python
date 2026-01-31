import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Hey Welcome to RPS Game!")
game_on = [rock, paper, scissors]
system_chosen = random.choice(game_on)

gamer_chosen = input("What do you choose? Type 0 for Rock,"
                     "1 for Paper or 2 for Scissors.\n")
if gamer_chosen == "0" and system_chosen == rock:
    print(game_on[0])
    print("It's a draw.")
elif gamer_chosen == "1" and system_chosen == paper:
    print(game_on[1])
    print("It's a draw.")
elif gamer_chosen == "2" and system_chosen == scissors:
    print(game_on[2])
    print("It's a draw.")
elif gamer_chosen == "0" and system_chosen == paper:
    print(game_on[0])
    print("You lose.")
elif gamer_chosen == "0" and system_chosen == scissors:
    print(game_on[0])
    print("You won!")
elif gamer_chosen == "1" and system_chosen == rock:
    print(game_on[1])
    print("You won!")
elif gamer_chosen == "1" and system_chosen == scissors:
    print(game_on[1])
    print("You lose.")
elif gamer_chosen == "2" and system_chosen == rock:
    print(game_on[2])
    print("You lose.")
elif gamer_chosen == "2" and system_chosen == paper:
    print(game_on[2])
    print("You won!")
else:
    print("You typed an invalid input. Try again.")
print(system_chosen)
print("Computer chose.")
