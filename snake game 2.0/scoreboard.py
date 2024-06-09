from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("/Users/dipra/OneDrive/Desktop/Python/01_AU_100/Day-24 (file io)/snake game 2.0/data.txt") as data:
            self.high_score = int(data.read())

        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/dipra/OneDrive/Desktop/Python/01_AU_100/Day-24 (file io)/snake game 2.0/data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self, increase_score):
        self.score += increase_score
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)