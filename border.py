from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(width=10)
        self.hideturtle()
        self.penup()
        self.goto(0, -300)
        self.pendown()
        self.goto(0, 300)