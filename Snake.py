from turtle import Turtle
import random,time
SET_POSITION=[(0,0),(-20,0),(-40,0)]
class Snk():
    #initializing snake
    def __init__(self):
        self.segments=[]
        self.create()
        self.head1=0
        self.count=0
        self.head=self.segments[0]
        self.lastsegpos=()
        
    def create(self):
        
        for p in SET_POSITION:
            ns= Turtle("square")
            ns.color("white")
            ns.penup()
            ns.goto(p)
            self.segments.append(ns)
  #Actionlisteners and snake direction
    def move(self):
        self.lastsegpos=self.segments[-1].position()
        for seg in range(len(self.segments)-1,0,-1):
            x=self.segments[seg-1].xcor()
            y=self.segments[seg-1].ycor()
            self.segments[seg].goto(x,y)
        self.segments[0].forward(20)
        return self.segments[0]
    def new(self):
        pass
        
    def up(self):
        if self.head1!=270:
            self.segments[0].setheading(90)
            self.head1=90
    def d(self):
        if self.head1!=90:
            self.segments[0].setheading(270)
            self.head1=270
    def l(self):
        if self.head1!=0:
            self.segments[0].setheading(180)
            self.head1=180
    def r(self):
        if self.head1!=180:
            self.segments[0].setheading(0)
            self.head1=0
    def increase_size(self):
        ns= Turtle("square")
        ns.color("white")
        ns.penup()
        ns.goto(self.lastsegpos)
        self.segments.append(ns)
        
  #Creating food randomly      
class Food():
    def __init__(self):
        self.food=Turtle()
        self.food.shape("circle")
        self.food.penup()
        self.food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food.color("green")
        self.food.speed("fastest")
        self.x=random.randint(-270,270)
        self.y=random.randint(-270,270)
        self.food.goto(self.x,self.y)
    def refresh(self):
        self.x=random.randint(-270,270)
        self.y=random.randint(-270,275)
        self.food.goto(self.x,self.y)
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,290)
        self.write(f"Score-{self.score}",align="center",font=("Ärial",14,"normal"))
    def refresh(self):
        self.clear()
        self.write(f"Score-{self.score}",align="center",font=("Ärial",14,"normal"))
    def restart(self):
        self.score=0
class Wall():
    def __init__(self):
        self.dimensions=[300,-300,300,-300]
        tur=Turtle()
        tur.hideturtle()
        tur.penup()
        tur.goto(-290,290)
        tur.pd()
        tur.pencolor("white")
        tur.pensize(2)
        tur.goto(290,290)
        tur.goto(290,-290)
        tur.goto(-290,-290)
        tur.goto(-290,290)
    def gameover():
        tim=Turtle()
        tim.shapesize(2, 2, 2)
        #tim.hideturtle()
        tim.color("red")
        tim.write("GAMEOVER",align="center",font=("Arial",12,"bold"))
        tim.penup()
        tim.goto(0,-20)
        tim.showturtle()
        tim.pendown()
        #tim.write("click y to restart and n to exit")
        
    def hit(self,snake):
        for i in snake.head.position():
            if i>280 or i<-280:
                Wall.gameover()
                return False
                
        for i in snake.segments[1::]:
            if snake.head.distance(Turtle.pos(i))<5:
                Wall.gameover()
                return False
        return True