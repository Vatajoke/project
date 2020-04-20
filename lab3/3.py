from graph import *


def window(x1, y1, x2, y2):
    brushColor(71, 220, 238)
    rectangle(x1, y1, x2, y2)
    penColor(214, 242, 245)
    penSize(8)
    line(x1-4, y1, x2, y1)
    line(x2, y2, x2, y1-4)
    line(x1-4, y2, x2+4, y2)
    line(x1, y1, x1, y2)
    x_midle = (x2 + x1) / 2
    y_midle = (y2 + y1) / 3
    line(x_midle, y1, x_midle, y2)
    line(x1, y_midle, x2, y_midle)


brushColor(95, 52, 13)
rectangle(0, 0, 500, 250)
brushColor(125, 102, 8)
rectangle(0, 250, 500, 600)

window(120, 20, 240, 200)
window(320, 20, 440, 200)
window(-60, 20, 60, 200)


run()