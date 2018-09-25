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

annie.left(132)
for i in range(4):
    annie.forward(100)
    annie.left(72)

annie.color("red")
annie.forward(100)

for i in range(5):
    annie.left(60)
    annie.forward(100)

turtle.done()
