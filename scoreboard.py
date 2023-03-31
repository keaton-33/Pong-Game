from turtle import Turtle


class Scoreboard:
    def __init__(self):
        # Creates 2 objects within the class and moves them to different spots on the screen
        self.p1_score = Turtle()
        self.p1_score.hideturtle()
        self.p1_score.penup()
        self.p1_score.speed(0)
        self.p1_score.color("white")
        # self.p1_score.score = 0
        self.p1_score.goto(-75, 275)
        self.score1 = 0

        self.p2_score = Turtle()
        self.p2_score.hideturtle()
        self.p2_score.penup()
        self.p2_score.speed(0)
        self.p2_score.color("white")
        # self.p2_score.score = 0
        self.p2_score.goto(75, 275)
        self.score2 = 0

        self.print_score()

    def print_score(self):
        self.p1_score.clear()
        self.p2_score.clear()
        self.p1_score.write(arg=str(self.score1), align="center", font=("Impact", 48, "bold"))
        self.p2_score.write(arg=str(self.score2), align="center", font=("Impact", 48, "bold"))