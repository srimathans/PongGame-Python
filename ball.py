from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.dx = 10
        self.dy = 10
        self.create_ball()

    def create_ball(self):
        self.shape('circle')
        self.penup()
        self.shapesize(1,1)
        self.color('red')

    def restart(self):
        self.setpos(0, 0)
        self.dx *= -1

    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

    def bounce_wall(self):
        self.dy *= -1

    def bounce_paddle(self):
        self.dx *= -1

