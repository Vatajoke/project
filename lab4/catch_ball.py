from tkinter import *
from random import randrange as rnd, choice


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
canv.score = Label(text=0, bg='black', fg='white', width=50, font=12)
canv.score.pack()

colors = ['red', 'orange', 'yellow', 'green', 'blue']


def new_ball():
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x-r, y-r, x+r, y+r, fill = choice(colors), width=0)
    root.after(1000, new_ball)


h = 0


def click(event):
    global h
    longer = (((x - event.x)**2) + ((y - event.y)**2))**0.5
    if longer < r:
        for i in range(1):
            h += 1
            canv.score.configure(text=h)


new_ball()

canv.bind('<Button-1>', click)
mainloop()