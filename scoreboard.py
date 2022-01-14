from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.scoreRight = 0
        self.scoreLeft = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score = {self.scoreLeft} : {self.scoreRight}', move=False, align=ALIGNMENT, font=FONT)

    #  when right paddle scores, increase score by one point
    def increase_score_right(self):
        self.scoreRight += 1
        self.clear()
        self.update_scoreboard()

    #  when left paddle scores, increase score by one point
    def increase_score_left(self):
        self.scoreLeft += 1
        self.clear()
        self.update_scoreboard()

    #  displays final score
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!\nFinal score...\n     {self.scoreLeft} : {self.scoreRight}", move=False, align=ALIGNMENT, font=FONT)







