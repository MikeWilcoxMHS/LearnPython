import turtle

fred = turtle.Turtle()
fred.shape("turtle")
fred.color("black")
fred.speed(4)
wilma = turtle.Turtle()
wilma.shape("arrow")
wilma.color("blue")
wilma.speed(4)

def do_draw ():
    for i in range(0,4):
        fred.forward(150)
        fred.right(90)

def draw_square ():
    window = turtle.Screen()
    window.bgcolor("red")
    do_draw()
    fred.penup()
    fred.goto(50,30)
    fred.pendown()
    do_draw()
    wilma.circle(100)
    window.exitonclick()


draw_square()


