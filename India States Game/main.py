import turtle
import pandas


screen = turtle.Screen()
screen.title("India States Game")
image = "india_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("india_states_sheet1.csv")
state_list_india = data.State.to_list()

map_writing = turtle.Turtle()
map_writing.hideturtle()
map_writing.penup()

correct_answers = []
missing_states = []


game_is_on = True
while game_is_on:
    give_answer = screen.textinput(
        f"{len(correct_answers)}/29 Correct States.",
        prompt="What's the another state's name?"
    )

    if give_answer is None:
        break

    give_answer = give_answer.title()

    if give_answer == "Exit":
        break

    if give_answer in state_list_india and give_answer not in correct_answers:

        correct_answers.append(give_answer)

        state_name = data[data.State == give_answer]
        x_cor = state_name.x.item()
        y_cor = state_name.y.item()

        map_writing.goto(x_cor, y_cor)
        map_writing.write(give_answer)

for state in state_list_india:
    if state not in correct_answers:
        missing_states.append(state)
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("learn_india's_state.csv")

# screen.exitonclick()
