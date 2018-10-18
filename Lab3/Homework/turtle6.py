import turtle

def draw_star(x,y,length):
    for i in range(50):
        turtle.goto(x,y)
        turtle.left(144)
        turtle.forward(length)

turtle.speed(0)
turtle.color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)