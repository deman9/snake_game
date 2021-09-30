from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("YOU DIE.", align=ALIGNMENT, font=FONT)
