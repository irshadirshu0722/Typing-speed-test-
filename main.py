import threading
import tkinter
from tkinter import Tk, Entry, Button, Label, filedialog,END
import tkinter as tk
import winsound

from PIL import Image, ImageTk, ImageDraw, ImageFont
import random
import time

#----------------------------------logic-----------------------------------------------
istyping=False
i=0
typingtime=0
current_word = ""
paragraph = ["A beautiful sunrise painted the sky with vibrant hues of orange and pink.","The quick brown fox jumps over the lazy dog. This sentence contains all the letters of the alphabet, making it a perfect test of your typing speed and accuracy","As the autumn leaves fell gently to the ground, the trees transformed into a breathtaking tapestry of red, orange, and gold. Nature's artwork provided a tranquil escape from the bustling world.","In the heart of the bustling city, people hurriedly moved through crowded streets, each with their own destination and purpose. Amid the chaos, a sense of unity and diversity thrived."]
starttime=0
def start_loop():
    global starttime
    starttime = time.time()
    speed_label.config(text="Your typing speed : ")
    entry.config(state="normal")
    isstarted.config(text="started" ,fg="green")
    status.config(text="")
    entry.delete(0,END)
    play_sound(10000)






def play_sound(freg):
    winsound.Beep(freg, 50)  #


def setspeed(word,starttime):
    timetaken = time.time()-starttime
    print(starttime,time.time(),word,timetaken)
    speed = round( word/ (timetaken/60),2)
    print("enter ",speed)
    speed_label.config(text=f"Your typing speed :{speed}W/m")
    isstarted.config(text="Completed")



def stop_loop():
    window.after_cancel(istyping)

def setpara():
    global  current_word
    current_word = random.choice(paragraph)
    speed_test_word.config(text=current_word)
    start.config(state="normal")
def onchange(event):
    global current_word
    entrytext = entry.get()
    if entrytext==current_word:
        setspeed(len(current_word.split()),starttime)

    elif entrytext[:len(entrytext)]==current_word[:len(entrytext)]:

        status.config(text="You're right",font=("Arial",20),fg="green")
    else:

        status.config(text="You're Wrong",font=("Arial",20),fg="red")
        play_sound(1000)









#------------------------------------UI--------------------------------------------------
window = Tk()
window.title("Typing Speed Test")
window.geometry("2000x600")
window.configure(bg="white")


label = Label(font=("Arail",40),text="Typing speed testing App")
label.grid(column = 0,row=0)

isstarted = Label(font=("Arail",15),text="Not started yet" ,fg="red")
isstarted.grid(column=0,row=2,pady=10)



speed_test_word = Label(font=("Arail",15),text="",bg="white")
speed_test_word.grid(column=0,row=3)


entry = Entry(width=40,state="disabled")
entry.bind("<KeyRelease>",onchange)
entry.grid(column=0,row=4,padx=20)

status = Label(text="",bg="white")
status.grid(column=0,row=5)

speed_label = Label(font=("Arail",30),text="Your typing speed : ",bg="white")
speed_label.grid(column = 0,row=6,pady=50)

getword = Button(text="Get paragraph",command=setpara,font=('Arial',20),bg="orange")
getword.grid(column=0,row=7)

start=Button(text="Start Typing",command=start_loop,font=('Arial',20),bg="green",state="disabled",fg="white",)
start.grid(column=0,row=8,pady=10,padx="900")


window.mainloop()
