# python program to create a small paint application

# import everything from tkinter
from tkinter import *

# create a GUI window
window = Tk()

# function to draw oval shaped points
def callback(event):
    c.create_oval(event.x - 5, event.y - 5,
                  event.x + 5, event.y + 5, fill="#558832")


# function to drag and draw anything
def draw(event):
    c.create_oval(event.x - 5, event.y - 5,
                  event.x + 5, event.y + 5, fill="#000000")


# function to draw a rectangle
def drawRectangle(event):
    global draw, x1, y1
    if draw:
        c.create_rectangle(x1, y1, event.x, event.y, fill="Red")
        draw = False
    else:
        x1 = event.x
        y1 = event.y
        draw = True


# create a canvas where we can draw and specify its width and height
c = Canvas(window, width=400, height=400)
# show the canvas
c.pack()
# when we left click the mouse, callback function is called
c.bind("<Button-1>", callback)
# when be drag after left clicking the mouse, draw function is called
c.bind("<B1-Motion>", draw)
# when we right click the mouse, drawRectangle function is called
# initially x and y co-ordinates of starting point is 0
# once we right click initial co-ordinates changes
# after drawing each rectangle draw is set to false
c.bind("<Button-3>", drawRectangle)
draw = False
x1 = 0
y1 = 0
# display the window
window.mainloop()