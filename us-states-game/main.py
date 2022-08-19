import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title =f"{len(correct_states)}/50 states correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        new_data = pandas.DataFrame([state for state in all_states if state not in correct_states])
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        correct_states.append(answer_state)
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        state_data = data[data.state == answer_state]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(answer_state)


