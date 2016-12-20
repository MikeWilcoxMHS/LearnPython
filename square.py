import turtle

fred = turtle.Turtle()
fred.shape("turtle")
fred.color("black")
fred.speed(1)

def do_draw ():
    for i in range(0,4):
        fred.forward(150)
        fred.right(90)

def draw_square ():
    window = turtle.Screen()
    window.bgcolor("red")
    do_draw()
    fred.goto(50,30)
    do_draw()
    window.exitonclick()

draw_square()
