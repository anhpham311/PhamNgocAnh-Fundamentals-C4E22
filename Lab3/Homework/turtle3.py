import turtle

def draw_square(turtle, length, color):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
        turtle.color(color)


annie = turtle.Turtle()
draw_square(annie, 70, "green")

turtle.done()