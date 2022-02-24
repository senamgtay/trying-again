import random
from math import *
import turtle
die=turtle.Turtle()
die.speed(0)
die.color("darkred")

win=turtle.Screen()
win.setup(width=0.90, height=0.90)

#Our Dice
def drawcircle(a,b,myTurtle):
    myTurtle.up()
    myTurtle.goto(a,b-10)
    myTurtle.down()
    myTurtle.width(1)
    myTurtle.fillcolor("white")
    myTurtle.begin_fill()
    myTurtle.circle(10)
    myTurtle.end_fill()
    myTurtle.hideturtle()


def face1(x,y,die):
    die.width(4)
    die.up()
    die.goto(x,y)
    die.down()
    die.fillcolor("darkred")
    die.begin_fill()
    for i in range(4):
        die.forward(100)
        die.right(90)
    die.end_fill()

    '''lists=list(die.position())
    x= round(lists[0],1)
    y=round(lists[1],1)'''

     #circle 1 loc
    midx=x+(50)
    midy=y-(50)
   
    drawcircle(midx,midy,die)


def face2(x,y,die):
    die.width(4)
    die.up()
    die.goto(x,y)
    die.down()
    die.fillcolor("darkred")
    die.begin_fill()
    for i in range(4):
        die.forward(100)
        die.right(90)
    die.end_fill()
        

    lists=list(die.position())
    x=round(lists[0],1)
    y=round(lists[1],1)

   #circle 1 face 4 location
    loc1x=x+20 
    loc1y=y-20

   #circle 2 face 4 location
    loc2x=loc1x+60
    loc2y=loc1y-60

    drawcircle(loc1x,loc1y,die)
    drawcircle(loc2x,loc2y,die)

#face3
def face3(x,y,die):
    die.width(4)
    die.up()
    die.goto(x,y)
    die.down()
    die.fillcolor("darkred")
    die.begin_fill()
    for i in range(4):
        die.forward(100)
        die.right(90)
    die.end_fill()

    midx=x+(50)
    midy=y-(50)
   

    drawcircle(midx,midy,die)

    die.up()
    die.goto(x,y)

    rightx=x+80
    righty=y-20

    drawcircle(rightx,righty,die)

    die.up()
    die.goto(x,y)

    leftx=x+20
    lefty=y-80

    drawcircle(leftx,lefty,die)

def face4(x,y,die):
    die.width(4)
    die.up()
    die.goto(x,y)
    die.down()
    die.fillcolor("darkred")
    die.begin_fill()
    for i in range(4):
        die.forward(100)
        die.right(90)
    die.end_fill()
    
    lists=list(die.position())
    x=round(lists[0],1)
    y=round(lists[1],1)

    #circle 1 face 4 location
    loc1x=x+20
    loc1y=y-20

    #circle 2 face 4 location
    loc2x=loc1x+60
    loc2y=loc1y

    #circle 3 face 4 location
    loc3x=loc2x
    loc3y=loc2y-60

   #circle 4 face 4 location
    loc4x=loc3x-60
    loc4y=loc3y


    drawcircle(loc1x,loc1y,die)
    drawcircle(loc2x,loc2y,die)
    drawcircle(loc3x,loc3y,die)
    drawcircle(loc4x,loc4y,die)

#face 5
def face5(x,y,die):
    die.width(4)
    die.up()
    die.goto(x,y)
    die.down()
    die.fillcolor("darkred")
    die.begin_fill()
    for i in range(4):
        die.forward(100)
        die.right(90)
    die.end_fill()
    
    die.up()
    die.goto(x,y)

    midx=x+(50)
    midy=y-(50)

    drawcircle(midx,midy,die)

    die.up()
    die.goto(x,y)

    rightx=x+80
    righty=y-20

    drawcircle(rightx,righty,die)

    die.up()
    die.goto(x,y)

    leftx=x+20
    lefty=y-80

    drawcircle(leftx,lefty,die)

    bottomrightx=x+80
    bottomrighty=y-80

    drawcircle(bottomrightx,bottomrighty,die)

    die.up()
    die.goto(x,y)

    topleftx=x+20
    toplefty=y-20

    drawcircle(topleftx,toplefty,die)


def face6(x,y,die):
    die.width(4)
    die.up()
    die.goto(x,y)
    die.down()

    die.fillcolor("darkred")
    die.begin_fill()
    for i in range(4):
        die.forward(100)
        die.right(90)
    die.end_fill()

    lists=list(die.position())
    x=round(lists[0],1)
    y=round(lists[1],1)

    #circle 1 face 4 location
    loc1x=x+20
    loc1y=y-20

    #circle 2 face 4 location
    loc2x=loc1x
    loc2y=loc1y-30

    #circle 3 face 4 location
    loc3x=loc2x
    loc3y=loc2y-30

    #circle 4 face 4 location
    loc4x=loc3x+60
    loc4y=loc3y

    #circle 4 face 5 location
    loc5x=loc4x
    loc5y=loc4y+30

    #circle 4 face 6 location
    loc6x=loc5x
    loc6y=loc5y+30


    drawcircle(loc1x,loc1y,die)
    drawcircle(loc2x,loc2y,die)
    drawcircle(loc3x,loc3y,die)
    drawcircle(loc4x,loc4y,die)
    drawcircle(loc5x,loc5y,die)
    drawcircle(loc6x,loc6y,die)




#code for randomizing and finding sum
n=random.randint(2,5)
d=random.randint(1,6)
sumofvalues=0
for i in range(n):
    d=random.randint(1,6)
    if d==1:
        face1(350,100,die)
    if d==2:
        face2(150,-100,die)
    if d==3:
        face3(0,100,die)
    if d==4:
        face4(0,-100,die)
    if d==5:
        face5(150,100,die)
    if d==6:
        face6(350,-100,die)
    sumofvalues+=d

import tkinter as tk
from tkinter import simpledialog

ROOT= tk.Tk()

ROOT.withdraw()

name = simpledialog.askinteger(title="How Fast Can you Add?",
                                  prompt="Enter your answer:")
if name==d:
    print("Congratulations,You can add really fast")
else:
    print("Better luck next time")



#compares the sum to the input
