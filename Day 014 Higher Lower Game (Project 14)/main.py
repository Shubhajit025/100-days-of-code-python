import random
from art import logo
from art import vs
from game_data import data

# Printing Logo at the starting of the game 👇:
print(logo)

# Taking random data from Game data and store inside a variable 👇:
option_b = random.choice(data)
score = 0

game_not_end = True

# Using While loop for continue progression of game when player winning the game. If player lost game ended there 👇:
while game_not_end:
    # Set the previous option B as the new option A for the next round 👇:
    option_a = option_b
    option_b = random.choice(data)

    while option_a == option_b:
        option_b = random.choice(data)


    # For first value before compare, extract from a listed data where inside the list there is dict by using key 👇:
    a_name = option_a["name"]
    a_followers = option_a["follower_count"]
    a_description = option_a["description"]
    a_country = option_a["country"]

    # For second value before compare, extract from a listed data where inside the list there is dict by using key 👇:
    b_name = option_b["name"]
    b_followers = option_b["follower_count"]
    b_description = option_b["description"]
    b_country = option_b["country"]

    Compare_A = f"Compare A: {a_name}, a {a_description}, from {a_country}."
    Against_B = f"Against B: {b_name}, a {b_description}, from {b_country}."

    print(Compare_A)
    print(vs)
    print(Against_B)

    user_choice = input("Who has more followers? Type 'A' or 'B' : ").lower()

    # Compare between two data respect to their followers count 👇:
    if a_followers > b_followers:
        correct_input = "a"
    else:
        correct_input = "b"

    if user_choice == correct_input:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_not_end = False
