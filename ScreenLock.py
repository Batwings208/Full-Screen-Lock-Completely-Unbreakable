#Use wisely
#For educational Purposes
#Created By Batwings208
#You are responsible for your actions
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

label1 = ttk.Label(tk, text='Facial Recognition Required for further access', font='Futura 8')
label1.place(relx=0.0, rely=0.0, anchor=NW)

button1 = ttk.Button(tk, text='Begin Facial Recognition', command=tk.destroy)
button1.place(width=200, height=40, relx=0.5, rely=0.5, anchor=CENTER)

mainloop()
