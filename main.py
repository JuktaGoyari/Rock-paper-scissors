#initialize Libraries
from tkinter import *
import random

# Initialize Window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock,Paper,Scissors')
root.config(bg ='light green')
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'violet').pack()

#For User Choice
user_take = StringVar()
Label(root, text = 'choose any one: rock, paper ,scissors' , font='arial 15 bold', bg = 'pink').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'light blue').place(x=90 , y = 130)

#For Computer Choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

#Function to Start Game
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

#Function to Reset    
def Reset():
        Result.set("")
        user_take.set("")

#Function to Exit
def Exit():
        root.destroy()

#Define Buttons    
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='light blue',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='red' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='red' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='red' ,command = Exit).place(x=230,y=310)


root.mainloop()