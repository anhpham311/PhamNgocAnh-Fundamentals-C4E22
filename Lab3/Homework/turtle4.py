import turtle
def draw_square(turtle, length, color):
    turtle.forward(length)
    turtle.color(color)

annie = turtle.Turtle()

for i in range(30):
    draw_square(annie, i * 5, 'red')
    annie.left(17)
    annie.penup()
    annie.forward(i * 2)
    annie.pendown()

turtle.done()
