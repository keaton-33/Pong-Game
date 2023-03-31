from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(0.5, 0.5)
        self.color("white")
        self.penup()
        self.speed(10)
        self.ball_setup()
        # wall_angle is the direction the ball should go instead if the ball bounces. Calculated from paddle_bounce
        self.wall_angle = 0
        # wall_angle2 is in case the ball bounces off a wall twice before reaching the next paddle
        self.wall_angle2 = 0

    def move(self):
        self.forward(10)

    def ball_setup(self):
        self.setposition(0, 0)
        random_right = 0 + random.randint(0, 25) * random.choice((1, -1))
        random_left = 180 + random.randint(0, 25) * random.choice((1, -1))
        self.setheading(random.choice((random_right, random_left)))
        # return float(random.choice((random_right, random_left)))

    def paddle_bounce(self, y_hitbox):
        y_center = y_hitbox[0] + 35
        y_cor = self.ycor()
        heading = self.heading()
        # If ball is going left
        if 90 < heading < 270:
            # If ball hit top of paddle
            if y_cor - y_center > 0:
                if abs(y_cor - y_center) < 5:
                    self.setheading(5)
                    self.wall_angle = 355
                elif abs(y_cor - y_center) < 15:
                    self.setheading(15)
                    self.wall_angle = 345
                elif abs(y_cor - y_center) < 25:
                    self.setheading(30)
                    self.wall_angle = 330
                elif abs(y_cor - y_center) <= 35:
                    self.setheading(45)
                    self.wall_angle = 315
            # Else ball hit bottom of paddle
            else:
                if abs(y_cor - y_center) < 5:
                    self.setheading(355)
                    self.wall_angle = 5
                elif abs(y_cor - y_center) < 15:
                    self.setheading(345)
                    self.wall_angle = 15
                elif abs(y_cor - y_center) < 25:
                    self.setheading(330)
                    self.wall_angle = 30
                elif abs(y_cor - y_center) < 35:
                    self.setheading(315)
                    self.wall_angle = 45
        # Else ball is going right
        else:
            # If ball hit top of paddle
            if y_cor - y_center > 0:
                if abs(y_cor - y_center) < 5:
                    self.setheading(175)
                    self.wall_angle = 185
                elif abs(y_cor - y_center) < 15:
                    self.setheading(165)
                    self.wall_angle = 195
                elif abs(y_cor - y_center) < 25:
                    self.setheading(150)
                    self.wall_angle = 210
                elif abs(y_cor - y_center) < 35:
                    self.setheading(135)
                    self.wall_angle = 225
            # Else ball hit bottom of paddle
            else:
                if abs(y_cor - y_center) < 5:
                    self.setheading(185)
                    self.wall_angle = 175
                elif abs(y_cor - y_center) < 15:
                    self.setheading(195)
                    self.wall_angle = 165
                elif abs(y_cor - y_center) < 25:
                    self.setheading(210)
                    self.wall_angle = 150
                elif abs(y_cor - y_center) < 35:
                    self.setheading(225)
                    self.wall_angle = 135

                    #     heading = self.heading()
    #     if heading < 180:
    #         if heading < 90:
    #             self.bounce_up(self.calc_severity(y_hitbox))
    #         else:
    #             self.bounce_up(self.calc_severity(y_hitbox))
    #     elif heading > 180:
    #         if heading < 90:
    #             self.bounce_down(self.calc_severity(y_hitbox))
    #         else:
    #             self.bounce_down(self.calc_severity(y_hitbox))
    #     else:
    #         self.setheading(self.random_heading())
    #
    # def calc_angle(self, y_hitbox):




        # if abs(self.ycor() - y_center) > 25:
        #     return 3
        # elif abs(self.ycor() - y_center) > 15:
        #     return 2
        # elif abs(self.ycor() - y_center) > 5:
        #     return 1
        # else:
        #     return 0

        # if heading < 90:
        #     new_angle = 180 + (0 - heading)
        # elif heading > 270:
        #     new_angle = 180 + (360 - heading)
        # elif 90 < heading < 270:
        #     new_angle = 180 - heading
        # self.setheading(new_angle)

    # def bounce_up(self, severity):
    #     heading = self.heading()
    #     max_angle = [5, 15, 30, 45]
    #     min_angle = [0, 5, 15, 30]
    #
    #
    #
    #     if heading < 90:
    #         if heading > 45:
    #             self.setheading(180 - max_angle[severity])
    #         elif heading > 30:
    #             self.setheading(round(180 - 30 / heading * max_angle[severity], 2))
    #         elif heading > 15:
    #             self.setheading(round(180 - 15 / heading * max_angle[severity], 2))
    #         elif heading > 5:
    #             self.setheading(round(180 - 5 / heading * max_angle[severity], 2))
    #         else:
    #             self.setheading(180 - min_angle[severity])
    #     else:
    #         if heading < 135:
    #             self.setheading(max_angle[severity])
    #         elif heading < 150:
    #             self.setheading(round(30 / heading * max_angle[severity], 2))
    #         elif heading < 165:
    #             self.setheading(round(15 / heading * max_angle[severity], 2))
    #         elif heading < 175:
    #             self.setheading(round(5 / heading * max_angle[severity], 2))
    #         else:
    #             self.setheading(min_angle[severity])

        # if 135 > heading > 45:
        #     if heading > 90: self.setheading(max_angle[severity])
        #     # self.setheading(something + max_angle[severity])
        # elif 150 > heading > 30:
        #     pass
        # elif 165 > heading > 15:
        #     pass
        # elif 175 > heading > 5:
        #     pass
        # else:
        #     pass

    # def bounce_down(self, severity):
    #     heading = self.heading()
    #     max_angle = [5, 15, 30, 45]
    #     min_angle = [0, 5, 15, 30]
    #
    #     if heading > 270:
    #         if heading < 315:
    #             self.setheading(180 - max_angle[severity])
    #         elif heading < 330:
    #             self.setheading(round(180 - 30 / heading * max_angle[severity], 2))
    #         elif heading < 345:
    #             self.setheading(round(180 - 15 / heading * max_angle[severity], 2))
    #         elif heading < 355:
    #             self.setheading(round(180 - 5 / heading * max_angle[severity], 2))
    #         else:
    #             self.setheading(180 - min_angle[severity])
    #     else:
    #         if heading > 255:
    #             self.setheading(max_angle[severity])
    #         elif heading > 210:
    #             self.setheading(round(30 / heading * max_angle[severity], 2))
    #         elif heading > 195:
    #             self.setheading(round(15 / heading * max_angle[severity], 2))
    #         elif heading > 185:
    #             self.setheading(round(5 / heading * max_angle[severity], 2))
    #         else:
    #             self.setheading(min_angle[severity])

    def wall_bounce(self):
        heading = self.heading()
        self.wall_angle2 = self.wall_angle
        self.setheading(self.wall_angle2)
        self.wall_angle = heading


