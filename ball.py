from turtle import Turtle
from time import sleep
BALL_SHAPE = "circle"
BALL_COLOR = "red"
BALL_SIZE = 0.5
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.home()
        self.penup()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.x_move = 5
        self.y_move = 5
        self.shapesize(stretch_wid=BALL_SIZE,stretch_len=BALL_SIZE)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def wall_baunce(self):
        self.y_move *= -1
    def ball_baunce(self):
        self.x_move *= -1
    def reset_position(self):
        sleep(2)
        self.ball_baunce()
        self.home()
