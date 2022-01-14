from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid= 5, stretch_len= 1)

    def move_up(self):
        current_y = self.ycor()
        current_x = self.xcor()
        if current_y < 240:
            self.goto(current_x, current_y + 30)
        else:
            pass

    def move_down(self):
        current_y = self.ycor()
        current_x = self.xcor()
        if current_y > -240:
            self.goto(current_x, current_y - 30)
        else:
            pass
