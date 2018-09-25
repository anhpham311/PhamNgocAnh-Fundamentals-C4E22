import turtle

annie = turtle.Turtle()

annie.color("red")
for i in range(3):
    annie.left(90)
    annie.forward(100)

annie.color("blue")
annie.left(150)
annie.forward(100)
annie.right(120)
annie.forward(100)

annie.left(130)
annie.forward(100)
annie.left(115)
annie.forward(100)

turtle.done()
