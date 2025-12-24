from turtle import Turtle
ALIGHMENT="center"
FONT=("Courier", 24, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:\dr.angela yu python course\day 20 and 21\snake_game\data.txt") as file:
            self.high_score=int(file.read())

        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} high_score:{self.high_score}", align=ALIGHMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGHMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



