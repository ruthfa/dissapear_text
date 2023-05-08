from tkinter import *
import time


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
timer = None



def delete_text():
    entry.delete("1.0", "end")

def start_time(event):
    global timer
    if timer:
        window.after_cancel(timer)
    countdown(5)


def countdown(count):
    global timer
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        delete_text()



window = Tk()
window.title("Start typing!")
window.config(height=600, width=600, padx=100, pady=50)

label = Label(text="Start typing!!", font=(FONT_NAME, 16, "bold"))
label.grid(column=1, row=0)

entry = Text(width=50, font=(FONT_NAME, 12, "bold"))
entry.grid(column=1, row=2)
entry.bind("<Key>", start_time)
#entry.bind("<Key>", reset_time, add="+")

window.mainloop()
