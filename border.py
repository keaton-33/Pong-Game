from turtle import Turtle


class Border:
    def __init__(self):
        self.net = Turtle()
        self.net.penup()
        self.net.speed(0)
        self.net.hideturtle()
        self.net.goto(0, -340)
        self.net.setheading(90)
        self.net.color("white")
        self.net.pensize(1)
        for i in range(14):
            self.net.pendown()
            self.net.forward(30)
            self.net.penup()
            self.net.forward(20)
