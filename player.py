from turtle import Turtle
NAME_COLOR = "white"
NAME_Y_POS = -290
PLAYER_NAME_COLOR = "white"
PLAYER_NAME_FONT_STYLE = "courier"
PLAYER_NAME_FONT_SIZE = 24
PLAYER_NAME_FONT_WEIGHT = "bold"
PLAYER_NAME_FONT_ALIGNMENT = "center"

class Player(Turtle):
    def __init__(self,name_x_pos,name):
        super().__init__()
        self.name = name
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color(NAME_COLOR)
        self.goto(name_x_pos,NAME_Y_POS)
        self.write(f"{self.name}", align=PLAYER_NAME_FONT_ALIGNMENT,
                   font=(PLAYER_NAME_FONT_STYLE, PLAYER_NAME_FONT_SIZE, PLAYER_NAME_FONT_WEIGHT))
    def winner(self):
        self.home()
        self.write(f"{self.name} Wins!", align=PLAYER_NAME_FONT_ALIGNMENT,
                   font=(PLAYER_NAME_FONT_STYLE, PLAYER_NAME_FONT_SIZE, PLAYER_NAME_FONT_WEIGHT))
