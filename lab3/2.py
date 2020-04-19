from graph import *

windowSize(500, 350)
brushColor(102, 204, 255)
rectangle(0, 0, 500, 150)
brushColor("blue")
rectangle(0, 150, 500, 230)
brushColor("yellow")
penColor("yellow")
rectangle(0, 230, 500, 350)
circle(450, 40, 30)
penColor("black")
brushColor("white")
for i in range(3):
    circle(100+(i*20), 50, 15)
for i in range(4):
    circle(90 + (i * 20), 70, 15)
run()
