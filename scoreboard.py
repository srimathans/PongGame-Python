from turtle import Turtle

COORD = [(50, 230), (-50, 230)]

class Scoreboard(Turtle):
    def __init__(self, k):
        super().__init__()
        self.score = -1
        self.create_score_turtle(k)

    def create_score_turtle(self, k):
        self.penup()
        self.hideturtle()
        self.shape('triangle')
        self.color('red')
        self.setpos(COORD[k])
        self.change_score()


    def change_score(self):
        self.score+=1
        self.clear()
        self.write(f'{self.score}', align='center', font=('Arial', 36, 'normal'))