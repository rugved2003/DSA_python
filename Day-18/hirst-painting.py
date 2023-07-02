import turtle as turtle_module
tim = turtle_module.Turtle()
import random

turtle_module.colormode(255)
color = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162), (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47), (55, 108, 89), (228, 167, 173), (189, 99, 107), (139, 33, 28), (194, 92, 79), (49, 40, 36), (228, 173, 166), (20, 92, 69), (177, 189, 212), (29, 62, 107), (113, 123, 155), (172, 202, 190), (51, 149, 193), (166, 200, 213)]
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100
# tim.bgcolor("black")

for dot_count in range(1,number_of_dots+1):
    tim.penup()
    tim.dot(20,random.choice(color))
    tim.penup()
    tim.forward(50)
    if dot_count %10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    tim.hideturtle()

screen = turtle_module.Screen()
screen.exitonclick()