import turtle
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(200)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    # TURTLE BRAD

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(5)
    brad.pensize(3)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

draw_art()
