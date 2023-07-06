#-----------------------------------------Pong Game------------------------------------------------#
"""
Date:- 06/07/2023
Developer:- Dinesh Singh

Description of the Game:- In this game we have 2 players where both can be human or 1 human and 1 computer. A ball is
bouncing along the up and down wall but left and right are not able to bounce here player have to bounce the ball if
if player miss the ball the opposition gain 1 point and vice versa. form detailed description refer to the documentation
of pong game:- https://en.wikipedia.org/wiki/Pong#:~:text=Pong%20is%20a%20two%2Ddimensional,a%20ball%20back%20and%20forth.
"""
#--------------------------------------------------------------------------------------------------#
# TODO 9 :- Keep Score
#--------------------------------------------------------------------------------------------------#
# TODO 1: Import Necessary Moudles (Done during development of the game)
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from player import Player
from border import Border
from time import sleep
import threading
#--------------------------------------------------------------------------------------------------#
LEFT_PLAYER_PADDLE_XPOS = -380
RIGHT_PLAYER_PADDLE_XPOS = 380
LEFT_PLAYER_NAME_XPOS = -250
RIGHT_PLAYER_NAME_XPOS = 250

SCOREBOARD_XPOS = 100
BALL_SPEED = 0.025
#--------------------------------------------------------------------------------------------------#
# TODO 3(a) :- Create the screen
playground = Screen()
playground.title("Bounce The Ball")
playground.bgcolor("black")
playground.setup(width=800,height=600)
playground.cv._rootwindow.resizable(False,False)
playground._root.iconbitmap("AppIcon.ico")
playground.tracer(0)
#--------------------------------------------------------------------------------------------------#
# TODO 9 :- Create player_name
lp_name,rp_name = "Left","Right"
lp_name = playground.textinput("Bouce The Ball","Enter Left Side Player Name").title()
rp_name = playground.textinput("Bouce The Ball","Enter Right Side Player Name").title()
left_player = Player(LEFT_PLAYER_NAME_XPOS,lp_name)
right_player = Player(RIGHT_PLAYER_NAME_XPOS,rp_name)
#--------------------------------------------------------------------------------------------------#
#TODO 11: Creat Boundry
border = Border()
#--------------------------------------------------------------------------------------------------#
# TODO 4 :- Create and move a paddles
l_paddle = Paddle(LEFT_PLAYER_PADDLE_XPOS)
r_paddle = Paddle(RIGHT_PLAYER_PADDLE_XPOS)
playground.listen()
playground.onkeypress(fun=l_paddle.move_up, key="w")
playground.onkeypress(fun=l_paddle.move_down, key="s")
playground.onkeypress(fun=r_paddle.move_up, key="Up")
playground.onkeypress(fun=r_paddle.move_down, key="Down")

#--------------------------------------------------------------------------------------------------#
# Trying to facilitate Simultaneous button action : But Thread Exception Occur
# left_up = threading.Thread(target=playground.onkeypress ,args=(l_paddle.move_up,'w'))
# left_down = threading.Thread(target=playground.onkeypress ,args=(l_paddle.move_down,'s'))
# right_up = threading.Thread(target=playground.onkeypress ,args=(r_paddle.move_up,'Up'))
# right_down = threading.Thread(target=playground.onkeypress ,args=(r_paddle.move_down,'Down'))
# right_up.start()
# right_down.start()
# left_up.start()
# left_down.start()
#--------------------------------------------------------------------------------------------------#
# TODO 5 :- Create the ball and make it move
ball = Ball()
sleep_time = BALL_SPEED
#--------------------------------------------------------------------------------------------------#
# TODO 5 :- Create the scoreboard for both player and place it
l_paddle_score = Scoreboard(-SCOREBOARD_XPOS)
r_paddle_score = Scoreboard(SCOREBOARD_XPOS)
is_game_over = False
#--------------------------------------------------------------------------------------------------#
while not is_game_over:
    playground.update()
    sleep(sleep_time)
    ball.move()
    # TODO 6 (a) :- Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # TODO 6 (b) :- Baunce the ball from wall
        ball.wall_baunce()
    # TODO 7 (a):- Detect the collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 360) or (ball.distance(l_paddle) < 50 and ball.xcor() < -360):
        # TODO 7 (b) :- Baunce the ball from paddle
        ball.ball_baunce()
        # TODO 7 (c) : Increase ball speed
        if sleep_time > 0.001:
            sleep_time -= 0.001
    # TODO 8 (a) :- Detect when l_paddle misses
    if ball.xcor() < -400:
        sleep_time = BALL_SPEED
        ball.reset_position()
        r_paddle_score.update_scoreboard()
    # TODO 8 (b) :- Detect when l_paddle misses
    if ball.xcor() > 400:
        sleep_time = BALL_SPEED
        l_paddle_score.update_scoreboard()
        ball.reset_position()
    # TODO 10 (a) : Check Left Player for win!
    if l_paddle_score.get_score() == 5:
        border.clear()
        left_player.clear()
        right_player.clear()
        left_player.winner()
        is_game_over = True
    # TODO 10 (b) : Check Player_2 for win!
    if r_paddle_score.get_score() == 5:
        border.clear()
        left_player.clear()
        right_player.clear()
        right_player.winner()
        is_game_over = True
#--------------------------------------------------------------------------------------------------#
# TODO 3(b) : Make Screen Visible until we click on it
playground.exitonclick()
#--------------------------------------------------------------------------------------------------#
