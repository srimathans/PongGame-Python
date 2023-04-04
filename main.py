from turtle import Screen
import turtle
from paddle import Paddle
from ball import Ball
from dashedline import Dashedline
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor('black')
my_screen.title('Pong')
my_screen.tracer(0)


my_paddleright = Paddle(0)
my_paddleleft = Paddle(1)
my_ball = Ball()
my_dashedline = Dashedline()
my_scoreright = Scoreboard(0)
my_scoreleft = Scoreboard(1)

my_screen.listen()
my_screen.onkeypress(my_paddleright.move_up, 'Up')
my_screen.onkeypress(my_paddleright.move_down, 'Down')
my_screen.onkeypress(my_paddleleft.move_up, 'q')
my_screen.onkeypress(my_paddleleft.move_down, 'a')

my_dashedline.draw()
speed = 0.07
while True:
    my_screen.update()
    time.sleep(speed)



    my_ball.move()


    wall_y = my_ball.ycor()
    if wall_y > 280 or wall_y < -280:
        my_ball.bounce_wall()

    dis1 = my_ball.distance(my_paddleright)
    dis2 = my_ball.distance(my_paddleleft)
    if (dis1 < 50 and my_ball.xcor() > 340) or (dis2 < 50 and my_ball.xcor() < -340):
        my_ball.bounce_paddle()
        speed *= 0.99


    if (my_ball.xcor() > 380 and dis1 > 30):
        my_scoreleft.change_score()
        my_ball.restart()
        speed = 0.07
    if (my_ball.xcor() < -380 and dis2 > 30):
        my_scoreright.change_score()
        my_ball.restart()
        speed = 0.07


turtle.done()






