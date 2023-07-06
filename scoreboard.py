from turtle import Turtle
SCOREBOARD_COLOR = "white"
SCOREBOARD_FONT_STYLE = "courier"
SCOREBOARD_FONT_SIZE = 60
SCOREBOARD_FONT_WEIGHT = "bold"
SCOREBOARD_FONT_ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self,X_POS):
        super().__init__()
        self.score = 0
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(X_POS,200)
        self.write(f"{self.score}", align=SCOREBOARD_FONT_ALIGNMENT, font=(SCOREBOARD_FONT_STYLE,SCOREBOARD_FONT_SIZE, SCOREBOARD_FONT_WEIGHT))
    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align=SCOREBOARD_FONT_ALIGNMENT, font=(SCOREBOARD_FONT_STYLE,SCOREBOARD_FONT_SIZE, SCOREBOARD_FONT_WEIGHT))

    def get_score(self):
        return self.score