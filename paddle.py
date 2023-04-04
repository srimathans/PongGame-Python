from turtle import Turtle
COORD =[(375, 0), (-375, 0)]

class Paddle(Turtle):
    def __init__(self, k):
        super().__init__()
        self.create_paddle(k)


    def create_paddle(self, k):
            self.shape('square')
            self.shapesize(1, 4)
            self.setheading(90)
            self.color('white')
            self.penup()
            self.setpos(COORD[k])


    def move_up(self):
        if self.ycor() > 270:
            return
        self.setheading(90)
        self.forward(20)
        # self.goto(self.xcor(), self.ycor()+20)


    def move_down(self):
        if self.ycor() < -270:
            return
        self.setheading(270)
        self.forward(20)
        # self.goto(self.xcor(), self.ycor()-20)