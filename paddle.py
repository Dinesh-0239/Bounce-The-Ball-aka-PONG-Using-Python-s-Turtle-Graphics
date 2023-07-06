from turtle import Turtle
PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1
STEP_SIZE = 20

class Paddle(Turtle,):
    def __init__(self,x_pos):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=PADDLE_WIDTH,stretch_len=PADDLE_HEIGHT)
        self.hideturtle()
        self.setpos(x=x_pos,y=0)
        self.showturtle()
    def move_up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(),self.ycor() + STEP_SIZE)
    def move_down(self):
        # self.maintain_direction()
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor() - STEP_SIZE)

