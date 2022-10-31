#Use wisely
#For educational Purposes
#Created By Batwings208
#You are responsible for your actions
#I expect a programmer to be using this as someone who doesn't wont understand the code, this is for you to figure out as its a potentially dangerous code
# so I am not explaing it for that reason
from tkinter import *
from tkinter import ttk
from pynput import *


"""
import pynput
import time

keyboard = pynput.keyboard.Listener(supress=True) # this here deactivates your keyboard
keyboard.start() # this is where ur keyboard will stop working

#make sure to have a way to kill the entire program and that will bring ur keyboard back online, if the program stays on, ur keyboard stays offline
"""

tk = Tk()
tk.attributes('-fullscreen', True)
tk.resizable(False, False)

label1 = ttk.Label(tk, text='DO NOT USE INTENTIONS OF HARM', font='Futura 8')
label1.place(relx=0.0, rely=0.0, anchor=NW)

button1 = ttk.Button(tk, text='Begin', command=tk.destroy)
button1.place(width=200, height=40, relx=0.5, rely=0.5, anchor=CENTER)

mainloop()
