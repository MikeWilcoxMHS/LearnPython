import turtle

def make_turtle(shape, color, speed):
    turt = turtle.Turtle()
    turt.shape(shape)
    turt.color(color)
    turt.speed(speed)
    return turt

def move_and_turn(turt, distance, angle):
    turt.forward(distance)
    turt.right(angle)

def draw_triangle(turt):
    turt.left(270)
    for i in range(3):
        move_and_turn(turt, 100, 120)

def draw_square(turt):
    for i in range(4):
        move_and_turn(turt, 100, 90)

def draw():
    fred = make_turtle("turtle", "green", 2)
    wilma = make_turtle("arrow", "pink", 2)
    dino = make_turtle("circle", "red", 5)

    window = turtle.Screen()
    window.bgcolor("black")
    draw_square(fred)
    draw_triangle(wilma)
    dino.circle(100)
    window.exitonclick()

draw()
