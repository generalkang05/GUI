from datetime import datetime
from tkinter import *

win = Tk()




win.geometry("1000x500")
win.title("what time?")
win.option_add("*Font", "맑은고딕 25")
win.configure(bg = "red")

def what_time():
    dnow = datetime.now()
    btn.config(text = dnow)

btn = Button(win)
btn.config(text = "현재 시각")
btn.config(width = 100, height = 10)
btn.config(command = what_time)


btn.pack()



win.mainloop()