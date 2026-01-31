import random
from art import logo

print(logo)
print("Welcome to the 'Number Guessing Game!' 🎴")
print("I am thinking of a number in between 1 to 100.\nAnd you have to guess the number. 🤔")


def easy():
    """Easy Gameplay."""

    print(logo)
    computer_thinking = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    game_not_end = True
    print("You have 10 attempts remaining to guess the number. 🥴")

    while game_not_end and attempts < 10:

        player_guess = int(input("Make a guess 👇: \n"))
        if player_guess > computer_thinking:
            attempts += 1
            max_attempts -= 1
            print(f"Too high.\nThink again. You have {max_attempts}/10 attempt left. 🤔")
            if max_attempts == 0:
                print(f"Computer thinking was : {computer_thinking}. You lost. 😢")
                game_not_end = False
        elif player_guess < computer_thinking:
            attempts += 1
            max_attempts -= 1
            print(f"Too low.\nThink again. You have {max_attempts}/10 attempt left. 🤔")
            if max_attempts == 0:
                print(f"Computer thinking was : {computer_thinking}. You lost. 😢")
                game_not_end = False
        elif player_guess == computer_thinking:
            attempts += 1
            max_attempts -= 1
            print(f"You win the game in {attempts} attempts. Still {max_attempts}/10 attempt left.")
            game_not_end = False

def hard():
    """Hard Gameplay."""

    print(logo)
    computer_thinking = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    game_not_end = True
    print("You have 5 attempts remaining to guess the number. 👀")

    while game_not_end and attempts < 5:

        player_guess = int(input("Make a guess 👇: \n"))
        if player_guess > computer_thinking:
            attempts += 1
            max_attempts -= 1
            print(f"Too high.\nThink again. You have {max_attempts}/5 attempt left. 🤔")
            if max_attempts == 0:
                print(f"Computer thinking was : {computer_thinking}. You lost. 😢")
                game_not_end = False
        elif player_guess < computer_thinking:
            attempts += 1
            max_attempts -= 1
            print(f"Too low.\nThink again. You have {max_attempts}/5 attempt left. 🤔")
            if max_attempts == 0:
                print(f"Computer thinking was : {computer_thinking}. You lost. 😢")
                game_not_end = False
        elif player_guess == computer_thinking:
            attempts += 1
            max_attempts -= 1
            print(f"You win the game in {attempts} attempts. Still {max_attempts}/5 attempt left.")
            game_not_end = False


play_game = True

while play_game:
    difficulty = input("Choose a difficulty. Type 'easy'😁 or 'hard'😎 Type below 👇: \n").lower()
    if difficulty == "easy":
        easy()
    elif difficulty == "hard":
        hard()

    play_or_not = input("Do you want to play the game : Type 'yes' or 'no' 👇:\n")
    if play_or_not == "no":
        print("Thanks for playing! 😉")
        play_game = False
    elif play_or_not == "yes":
        print("\n" * 20)
