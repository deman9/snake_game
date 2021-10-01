from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def reset_score(self):
        if self.score > self.high_score: 
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.clear()
        self.write_score()
        


    def load_high_score(self):
        with open('high_scores.txt', mode='r') as f:
            hscore = f.read()
            return int(hscore)

    def save_high_score(self):
        with open('high_scores.txt', mode='w') as f: 
            f.write(str(self.high_score))


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("YOU DIE.", align=ALIGNMENT, font=FONT)
