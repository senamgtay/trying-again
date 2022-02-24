 

import random
from math import *
import turtle
import sys 
import tkinter as tk
from tkinter import *
import winsound
import time

# drawcircle function draws standard circles need for a dice face
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

# drawsquare draws the standard square for the dice.
def drawsquare(x,y,dice):
    dice.width(4)
    dice.up()
    dice.goto(x,y)
    dice.down()
    dice.fillcolor("darkred")
    dice.begin_fill()
    for i in range(4):
        dice.forward(100)
        dice.right(90)
    dice.end_fill()

# Face functions draws the respective dice
def face1(x,y,dice):
    drawsquare(x,y,dice)

    #circle 1 location
    loc1x=x+(50)
    loc1y=y-(50)
   
    drawcircle(loc1x,loc1y,dice)

#face 2
def face2(x,y,dice):
    drawsquare(x,y,dice)

   #circle 1
    loc1x=x+20 
    loc1y=y-20

   #circle 2
    loc2x=loc1x+60
    loc2y=loc1y-60

    drawcircle(loc1x,loc1y,dice)
    drawcircle(loc2x,loc2y,dice)

#face 3
def face3(x,y,dice):
    drawsquare(x,y,dice)

    #circle 1
    loc1x=x+(50)
    loc1y=y-(50)

    #circle 2
    loc2x=x+80
    loc2y=y-20

    #circle 3
    loc3x=x+20
    loc3y=y-80

    drawcircle(loc1x, loc1y, dice)
    drawcircle(loc2x, loc2y, dice)
    drawcircle(loc3x,loc3y,dice)

#face 4
def face4(x,y,dice):
    drawsquare(x,y,dice)

    #circle 1
    loc1x=x+20
    loc1y=y-20

    #circle 2
    loc2x=loc1x+60
    loc2y=loc1y

    #circle 3
    loc3x=loc2x
    loc3y=loc2y-60

   #circle 4
    loc4x=loc3x-60
    loc4y=loc3y


    drawcircle(loc1x,loc1y,dice)
    drawcircle(loc2x,loc2y,dice)
    drawcircle(loc3x,loc3y,dice)
    drawcircle(loc4x,loc4y,dice)

#face 5
def face5(x,y,dice):
    drawsquare(x,y,dice)

    #circle 1
    loc1x=x+(50)
    loc1y=y-(50)

    # circle 2
    loc2x=x+80
    loc2y=y-20

    # circle 3
    loc3x=x+20
    loc3y=y-80

    # circle 4
    loc4x=x+80
    loc4y=y-80

    # circle 5
    loc5x=x+20
    loc5y=y-20

    drawcircle(loc1x, loc1y, dice)
    drawcircle(loc2x, loc2y, dice)
    drawcircle(loc3x, loc3y, dice)
    drawcircle(loc4x, loc4y, dice)
    drawcircle(loc5x,loc5y,dice)

#face 6
def face6(x,y,dice):
    drawsquare(x,y,dice)

    #circle 1
    loc1x=x+20
    loc1y=y-20

    #circle 2
    loc2x=loc1x
    loc2y=loc1y-30

    #circle 3
    loc3x=loc2x
    loc3y=loc2y-30

    #circle 4
    loc4x=loc3x+60
    loc4y=loc3y

    #circle 5
    loc5x=loc4x
    loc5y=loc4y+30

    #circle 6
    loc6x=loc5x
    loc6y=loc5y+30


    drawcircle(loc1x,loc1y,dice)
    drawcircle(loc2x,loc2y,dice)
    drawcircle(loc3x,loc3y,dice)
    drawcircle(loc4x,loc4y,dice)
    drawcircle(loc5x,loc5y,dice)
    drawcircle(loc6x,loc6y,dice)


# Dialog Box for when player wins
def popupWin():

    frame=Frame(root1)
    frame.pack()

    label = Label(frame,compound=tk.CENTER, text="Congratulations! You can add really fast.",pady=30)
    label.pack()
    button1=Button(frame,text="Replay", command=replay,padx=10)
    button1.pack(side=LEFT, padx=50)
    button2=Button(frame,text="Quit",command=Quit, padx=10)
    button2.pack(side=RIGHT)

# Dialog Box for when the player loses
def popupLose():

    frame=Frame(root1)
    frame.pack()

    label = Label(frame,compound=tk.CENTER, text="Oops! Better luck next time!", pady=10)
    label.pack()
    button1=Button(frame,text="Replay",command=replay,padx=10, pady=5)
    button1.pack(side=LEFT, padx=50)
    button2=Button(frame,text="Quit",command=Quit,padx=10, pady=5)
    button2.pack(side=RIGHT)

#Function for the quit button of the dialog box
def Quit():
    root1.destroy
    quit()

#Function for the submit button of the dialog box
def checkanswer():
    value=int(a.get())
    if value==sumofvalues:
        #Removes all the timer and entry box labels
        label.destroy()
        label2.destroy()
        a.destroy()
        buttonsub.pack_forget()
        #Displays the dialog box for winning the game
        popupWin()
        #Sound effects for a win
        winsound.PlaySound("win.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    else:
        #Removes all the timer and entry box labels
        label.destroy()
        label2.destroy()
        a.destroy()
        buttonsub.pack_forget()
        #Displays the dialog box for losing
        popupLose()
        #Sound effects for a lose
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

# Function for the timer.
def counter_label(label):
  def count():
    global counter
    if counter>0:
        counter -= 1
        label.config(text=str(counter))
        label.after(1000, count)

    else:
        winsound.PlaySound(None, winsound.SND_ASYNC)
        label.config(text="Time's Up!")
        label2.destroy()
        a.destroy()
        buttonsub.pack_forget()
        popupLose()
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
  count()

def replay():
    win.clear()
    root1.destroy()
    playgame()
    

def playgame():
    
    #Background Music for the game
    winsound.PlaySound("game.wav",winsound.SND_ASYNC|winsound.SND_ALIAS)

    #Creating a turtle screen and object
    global dice
    dice=turtle.Turtle()

    global win
    win=turtle.Screen()
    win.setworldcoordinates(-450,-450,450,450)
    dice.speed(100)

    # Title Screen
    dice.color("white")
    win.bgpic("bitmap.gif")
    dice.write("How Fast Can You Add",font=('Times New Roman',25,"bold"),align='center')
    dice.up()
    dice.goto(0,-20)
    dice.down()
    dice.hideturtle()
    dice.write("v1.0",font=('Times New Roman',10),align='center')
    time.sleep(3)
    win.clear()

    # Background for the game
    dice.color("darkred")
    win.bgpic("sol backd.gif")

    # Randomizing the number of die drawn
    global numdice
    numdice=random.randint(2,5)

    # Randomizing the faces of the die drawn
    global faced
    faced=random.randint(1,6)

    # Value of the die drawn
    global sumofvalues
    sumofvalues=0

    # List to store coordinates of the dice drawn
    listsxy=[]

    for i in range(numdice):
        faced=random.randint(1,6)
        if faced==1:
            xc=random.randrange(-350,351,150)
            yc=random.randrange(-350,351,150)

            while (xc,yc) in listsxy:
                xc=random.randrange(-350,351,150)
                yc=random.randrange(-350,351,150)

            listsxy.append((xc,yc))
            face1(xc,yc,dice)
        if faced==2:
            xc=random.randrange(-350,351,150)
            yc=random.randrange(-350,351,150)

            while (xc,yc) in listsxy:
                xc=random.randrange(-350,351,150)
                yc=random.randrange(-350,351,150)

            listsxy.append((xc,yc))
            face2(xc,yc,dice)
        if faced==3:
            xc=random.randrange(-350,351,150)
            yc=random.randrange(-350,351,150)

            while (xc,yc) in listsxy:
                xc=random.randrange(-350,351,150)
                yc=random.randrange(-350,351,150)

            listsxy.append((xc,yc))
            face3(xc,yc,dice)
        if faced==4:
            xc=random.randrange(-350,351,150)
            yc=random.randrange(-350,351,150)

            while (xc,yc) in listsxy:
                xc=random.randrange(-350,351,150)
                yc=random.randrange(-350,351,150)

            listsxy.append((xc,yc))
            face4(xc,yc,dice)
        if faced==5:
            xc=random.randrange(-350,351,150)
            yc=random.randrange(-350,351,150)

            while (xc,yc) in listsxy:
                xc=random.randrange(-350,351,150)
                yc=random.randrange(-350,351,150)

            listsxy.append((xc,yc))
            face5(xc,yc,dice)
        if faced==6:
            xc=random.randrange(-350,351,150)
            yc=random.randrange(-350,351,150)

            while (xc,yc) in listsxy:
                xc=random.randrange(-350,351,150)
                yc=random.randrange(-350,351,150)

            listsxy.append((xc,yc))
            face6(xc,yc,dice)
        sumofvalues+=faced

    # Creating the dialog box which will hold all necessary output's and input
    global root1
    root1= tk.Tk()
    root1.title("How Fast Can You Add?")
    root1.geometry("350x150")

    # Variable for the counter
    global counter
    counter = numdice*2

    # Label for the timer
    global label
    label = tk.Label(root1, fg="green")
    label.pack(pady=10)
    counter_label(label)

    # Label for the Entry box
    global label2
    label2=tk.Label(root1, text="Enter Your Answer:")
    label2.pack(pady=10)

    # Entry box
    global a
    a=Entry(root1, width=35)
    a.pack()

    # Submit button
    global buttonsub
    buttonsub=Button(root1,text="Submit",command=checkanswer)
    buttonsub.pack()

    root1.mainloop()

playgame()
