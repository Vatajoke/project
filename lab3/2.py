from graph import *

windowSize(500, 350)

brushColor("blue")
rectangle(0, 150, 500, 230)

brushColor("brown")
polygon([(420, 200), (420, 170), (480, 170)])
circle(290, 170, 30)
rectangle(290, 170, 420, 200)
line(260, 170, 290 ,170)
brushColor("blue")
penColor("blue")
rectangle(0, 150, 500, 170)

brushColor(102, 204, 255)
rectangle(0, 0, 500, 150)

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

penSize(5)
line(340, 170, 340, 80)
brushColor(240, 178, 122)
penSize(1)
polygon([(340, 170), (360, 125), (400, 125)])
polygon([(340, 80), (360, 125), (400, 125)])
penSize(3)
brushColor("white")
circle(435, 180, 7)

penSize(5)
penColor("brown")
line(90, 220, 90, 335)
penSize(1)
penColor("orange")
brushColor("orange")
polygon([(30, 220), (150, 220), (90, 180)])
penColor("black")
for i in range(30, 150, 15):
    line(90, 180, i, 220)
run()
