from turtle import Turtle

class Dashedline(Turtle):
    def __init__(self):
        super().__init__()
        self.create_line()

    def create_line(self):
        self.penup()
        self.setpos(0, -300)
        self.color('white')
        self.hideturtle()
        self.setheading(90)
        self.pensize(2)
        self.pendown()

    def draw(self):
        for i in range(70):
            if i%2==0:
                self.penup()
            else:
                self.pendown()
            self.forward(10)
