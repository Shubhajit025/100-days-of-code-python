def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
# turn_left(), turn_right(), at_goal(), front_is_clear(), right_is_clear(), move() those are premade functions.
