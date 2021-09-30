import turtle
import time
from tkinter import *

wn = turtle.Screen()
wn.title("Traffic Light")
wn.bgcolor("black")
canvas=wn.getcanvas()
can=Canvas(canvas,height=100,width=200,bg="black")

class Light():
    def __init__(self,x,y):
        self.p=turtle.Turtle()
        self.p.color("yellow")
        self.p.width(3)
        self.p.hideturtle()
        self.p.speed(0)
        self.p.penup()
        self.p.goto(x-30,y+60)
        self.p.pendown()
        self.p.fd(60)
        self.p.rt(90)
        self.p.fd(120)
        self.p.rt(90)
        self.p.fd(60)
        self.p.rt(90)
        self.p.fd(120)
        self.p.rt(90)

        self.color=""

        self.redl=turtle.Turtle()
        self.greenl=turtle.Turtle()
        self.timer_text=turtle.Turtle()

        self.redl.speed(0)
        self.greenl.speed(0)

        self.redl.color("grey")
        self.greenl.color("grey")

        self.redl.shape("circle")
        self.greenl.shape("circle")

        self.redl.penup()
        self.greenl.penup()

        self.redl.goto(x,y+40)
        self.greenl.goto(x,y-40)
    
    def change(self,color):
        self.redl.color("grey")
        self.greenl.color("grey")

        if(color=="red"):
            self.redl.color("red")
            self.color="red"      

        elif(color=="green"):
            self.greenl.color("green")
            self.color="green"

        else:
            print("ERROR")
    
    def timer(self):
        if(self.color=="red"):
            self.change("green")
            
        elif(self.color=="green"):
            self.change("red")
            
        else:
            print("ERROR")

    def timer_green(self):
        self.change("green")
        

    def timer_red(self):
        self.change("red")
        

class UI():
    def view(n):
        start = time.time()
        while time.time() - start < n:
            can.delete('all')
            y=str(int(time.time() - start))
            can.create_text(100,50,
            fill="yellow",
            font="Courier 30 bold",
            text=y)
            can.grid()
            wn.update()
    def text(x,y,t):
        Y=canvas.create_text(x,y,
        fill="yellow",
        font="Courier 20 bold",
        text=t)
        return(Y)
    def clear(y):
        canvas.delete(y)


