from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forewards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def clear():
    t.clear()
    t.home()


screen.listen()
screen.onkey(move_forewards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")

screen.exitonclick()