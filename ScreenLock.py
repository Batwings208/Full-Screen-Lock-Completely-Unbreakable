from tkinter import *
from tkinter import ttk
from pynput import *

tk = Tk()
tk.attributes('-fullscreen', True)
tk.resizable(False, False)

label1 = ttk.Label(tk, text='Facial Recognition Required for further access', font='Futura 8')
label1.place(relx=0.0, rely=0.0, anchor=NW)

button1 = ttk.Button(tk, text='Begin Facial Recognition', command=tk.destroy)
button1.place(width=200, height=40, relx=0.5, rely=0.5, anchor=CENTER)

mainloop()