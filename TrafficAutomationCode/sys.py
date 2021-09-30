import turtle
# import time
import random
from tkinter import *
from trafficlight import Light, UI
from vehicle_counting import Vehicle

def max2(x,m):
    y=x.copy()
    y.remove(m)
    a=max(y)
    return(x.index(a))

wn = turtle.Screen()
wn.title("Traffic Light")
wn.bgcolor("black")
canvas = wn.getcanvas()
can = Canvas(canvas, height=100, width=200, bg="black")

l1 = Light(-200, 0)
UI.text(-200, 100, "L1")

l4 = Light(200, 0)
UI.text(200, 100, "L4")

l2 = Light(0, -100)
UI.text(0, -200, "L2")

l3 = Light(0, 100)
UI.text(0, 200, "L3")

l1.change("green")
l2.change("red")
l4.change("red")
l3.change("red")

lights = [l1, l3, l4, l2]


n = Vehicle()
totalintensity = n.lcount()  # list
random.shuffle(totalintensity)
inten=totalintensity[:4]

e = UI.text(-200, 120, str(inten[0]))  # l1
w = UI.text(0, -220, str(inten[1]))  # l2
n = UI.text(0, 220, str(inten[3]))  # l3
s = UI.text(200, 120, str(inten[2]))  # l4


#count=[0]*4
#current=0
m = (max(inten))
i = inten.index(m)
cur=i
prev=0
count=0
while (True):
    
    if(count<2):
        lights[cur].timer()
        lights[prev].timer()
    else:
        cur=max2(inten,m)
        lights[cur].timer()
        lights[prev].timer()
        count=0
        

    if prev==cur:
            count+=1
            print(count)

    if m > 20:
        UI.view(m)
    else:        
        UI.view(10)
    
    print(cur,prev)
    random.shuffle(totalintensity)
    inten = totalintensity[:4]
    
    prev=cur
    m = (max(inten))
    i = inten.index(m)
    cur=i

    UI.clear(e)
    e = UI.text(-200, 120, str(inten[0]))  # l1
    UI.clear(w)
    w = UI.text(0, -220, str(inten[1]))  # l2
    UI.clear(n)
    n = UI.text(0, 220, str(inten[3]))  # l3
    UI.clear(s)
    s = UI.text(200, 120, str(inten[2]))  # l4


wn.listen()  # Listen for events
wn.mainloop()