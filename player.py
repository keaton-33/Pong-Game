from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.setheading(90)
        # Turtle size = 10 x 60
        self.turtlesize(0.5, 3.5)
        self.setpos(position)
        self.y_hitbox = (self.ycor() - 35, self.ycor() + 35)

    def cpu_move(self, ball_ycor):
        if abs(self.ycor() - ball_ycor) > 20:
            if self.ycor() < ball_ycor:
                self.forward(5)
            else:
                self.backward(5)

    def up(self):
        if self.ycor() < 320:
            self.forward(10)

    def down(self):
        if self.ycor() > -320:
            self.backward(10)

