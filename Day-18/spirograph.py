import random
import turtle as t

t.bgcolor('black')
t.colormode(255)
t.pensize(3)
t.speed("fastest")
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r,g,b)
    return colour

for i in range(12):
    for colour in random_colour():
        t.color(random_colour())
        t.circle(100)
        t.left(10)
    t.hideturtle()

screen = t.Screen()
screen.exitonclick()