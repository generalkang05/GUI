from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()




win.geometry("300x100")
win.option_add("*Font", "궁서 20")

ent = Entry(win)
ent.pack()

def ent_p():
    a = ent.get()
    print(a)

btn = Button(win)
btn.config(text = "로또 당첨 번호 확인")
btn.config(command = ent_p)
btn.pack()
win.mainloop()

url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=883"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
txt = soup.find("div", attrs = {"class", "win_result"}).get_text()
txt.split("\n")