from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        self.ball_move_speed = 0.05

    def move(self):
        x_coOrd = self.xcor() + self.x_move
        y_coOrd = self.ycor() + self.y_move
        self.goto(x_coOrd, y_coOrd)

    def bounce(self):
        self.y_move *= -1

    def bat(self):
        self.x_move *=-1
        self.ball_move_speed * 0.75

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1

    def game_over(self):
        self.goto(1000, 1000)





