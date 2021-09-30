import turtle
# import time
import random
import numpy as np

from tkinter import *
from trafficlight import Light, UI
from vehicle_counting import Vehicle

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


def utimer():
    l1.timer()
    l2.timer()
    l3.timer()
    l4.timer()
    UI.view(10)



n = Vehicle()
totalintensity = n.lcount()  # list
random.shuffle(totalintensity)
inten=totalintensity[:4]

# print(inten[:4])
e = UI.text(-200, 120, str(inten[0]))  # l1
w = UI.text(0, -220, str(inten[1]))  # l2
n = UI.text(0, 220, str(inten[3]))  # l3
s = UI.text(200, 120, str(inten[2]))  # l4

lights = [l1, l3, l4, l2]

flag=0
while (True):


    m = (max(inten))
    i = inten.index(m)
    if flag==0:
        current=i
    if m > 20:
        lights[i].timer_green()
        flag=1
        current=i
        for k in range(4):
              if k!=i:
                  lights[k].timer_red()

        UI.view(m)

    else:
        # UI.view(10)
        #count = [0] * 4
        pos=i
        values = np.array(inten)
        if i==current and flag==1:
            if inten.count(m) > 1:
                searchval = m
                ii = np.where(values == searchval)[0]
                i= ii[1]
            else:
                values = np.delete(values, pos)
                newmax=np.max(values)
                result=np.where(values == newmax)
                i=result[0][0]

        lights[i].timer_green()
        for k in range(4):
            if k != i:
                lights[k].timer_red()
        UI.view(10)
        # time.sleep(10)

    random.shuffle(totalintensity)
    inten = totalintensity[:4]

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