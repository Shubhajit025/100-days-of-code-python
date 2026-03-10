import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
# To get the co-ordinates for states inside the map. No need of under codes, we have our premade csv  file
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


# screen.exitonclick()


data = pandas.read_csv("50_states.csv")
states_data_list = data.state.to_list()

map_state_name_writer = turtle.Turtle()
map_state_name_writer.hideturtle()
map_state_name_writer.penup()

guessed_state = []
missing_states = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(
        title=f"Guess the State. {len(guessed_state)}/50 States Correct.",
        prompt="What's the another state's name?"
    )

    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        game_is_on = False

    if answer_state in states_data_list and answer_state not in guessed_state:
        guessed_state.append(answer_state)

        state_name_data = data[data.state == answer_state]
        x_cor = state_name_data.x.item()
        y_cor = state_name_data.y.item()

        map_state_name_writer.goto(x_cor, y_cor)
        map_state_name_writer.write(answer_state)

for state in states_data_list:
    if state not in guessed_state:
        missing_states.append(state)

new_csv_file = pandas.DataFrame(missing_states)
new_csv_file.to_csv("states_to_learn.csv")


# screen.exitonclick()
