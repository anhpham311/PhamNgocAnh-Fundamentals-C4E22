import turtle

annie = turtle.Turtle()

annie.color("green")
annie.speed(0)

for i in range(200):
    annie.circle(50)
    annie.right(60)
    annie.circle(50)

    annie.right(7)

turtle.done()
