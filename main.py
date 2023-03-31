from header import *
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
from border import Border
from time import sleep
FPS = 60

screen = Screen()
screen.setup(1280, 720)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player1 = Player((-600, 0))
player2 = Player((600, 0))
ball = Ball()
score = Scoreboard()
border = Border()

screen.listen()
screen.onkeypress(player1.up, "w")
screen.onkeypress(player1.down, "s")

screen.onkeypress(player2.up, "Up")
screen.onkeypress(player2.down, "Down")

x = 0
while True:
    screen.update()
    sleep(1 / FPS)
    ball.move()
    player2.cpu_move(ball.ycor())

    # Updates the current paddle hitboxes
    player1.y_hitbox = (player1.ycor() - 35, player1.ycor() + 35)
    player2.y_hitbox = (player2.ycor() - 35, player2.ycor() + 35)

    # Detect collision with paddles
    if -589 > ball.xcor() > -601:
        if player1.y_hitbox[0] <= ball.ycor() <= player1.y_hitbox[1]:
            ball.paddle_bounce(player1.y_hitbox)
    elif 589 < ball.xcor() < 601:
        if player2.y_hitbox[0] <= ball.ycor() <= player2.y_hitbox[1]:
            ball.paddle_bounce(player2.y_hitbox)

    # Detect collision with walls
    if ball.ycor() >= 355:
        ball.wall_bounce()
    elif ball.ycor() <= -355:
        ball.wall_bounce()

    # Detects if a player scored
    if ball.xcor() < -600:
        ball.ball_setup()
        score.score2 += 1
        score.print_score()
    elif ball.xcor() > 600:
        ball.ball_setup()
        score.score1 += 1
        score.print_score()


screen.exitonclick()
