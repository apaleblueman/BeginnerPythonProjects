import random
from turtle import Turtle ,Screen

colors_list = ['red', 'blue','green','yellow','cyan','pink']
isRaceOn = False
all_turtles = []

#creating a screen object
myScreen = Screen()

myScreen.setup(500,400)

user_bet = myScreen.textinput(title="Place your bet", prompt="turtle color");
if user_bet:
    isRaceOn = True

for i in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors_list[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + i*20)
    all_turtles.append(new_turtle)

while isRaceOn:
    for i in all_turtles:
        if i.xcor() > 230:
            isRaceOn = False
            winning_color = i.color()
            if winning_color == user_bet:
                print(f"You have won with {user_bet} turtle")
            else:
                print("you lost")
        rand_distance = random.randint(0, 10)
        i.forward(rand_distance)

myScreen.exitonclick()