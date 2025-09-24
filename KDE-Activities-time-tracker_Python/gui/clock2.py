import time
from tkinter import *
canvas = Tk()
canvas.title("Digital Clock")
canvas.geometry("350x200")
canvas.resizable(1,1)
label = Label(canvas, font=("Courier", 30, 'bold'), bg="blue", fg="white", bd =30)
label.grid(row =0, column=1)

def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   label.config(text=text_input)
   label.after(200, digitalclock)
digitalclock()
canvas.mainloop()