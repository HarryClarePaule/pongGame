from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

POSITIONS = ((350, 0), (-350, 0))

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Harry's Pong Game")
screen.tracer(0)

# set up scoreboard
scoreboard = Scoreboard()

# import paddles
paddleRight = Paddle((350,0))
paddleLeft = Paddle((-350, 0))

# import ball
ball = Ball()

screen.listen()
screen.onkeypress(paddleRight.move_up, 'Up')
screen.onkeypress(paddleRight.move_down, 'Down')
screen.onkeypress(paddleLeft.move_up, 'w')
screen.onkeypress(paddleLeft.move_down, 's')

game_is_on = True
while game_is_on:
    ball.move()

    # detect collision with top and bottom wall
    if ball.ycor() >= 300 or ball.ycor() < -300:
        ball.bounce()

    # detect collision with right paddle
    if ball.distance(paddleRight) < 50 and ball.xcor() > 340:
        ball.bat()

    # detect collision with right paddle
    if ball.distance(paddleLeft) < 50 and ball.xcor() < -340:
        ball.bat()

    # detect point score RHS
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.increase_score_left()

    # detect point score LHS
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.increase_score_right()

    # check score
    if scoreboard.scoreRight == 5 or scoreboard.scoreLeft == 5:
        game_is_on = False
        ball.game_over()

    time.sleep(ball.ball_move_speed)
    screen.update()
scoreboard.game_over()

screen.exitonclick()


