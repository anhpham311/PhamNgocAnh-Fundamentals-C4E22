import turtle

def draw_star(turtle, x, y, length):
    for i in range(5):
        turtle.left(144)
        turtle.forward(length)

annie = turtle.Turtle()
draw_star(annie, 190, 1, 70)

turtle.done()


