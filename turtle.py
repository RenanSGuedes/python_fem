# Import the library
from tkinter import *

# Create an instance of window
win = Tk()

# Set the geometry of the window
win.geometry("700x350")

C1 = Canvas(win, width=600, height=400)

# Coordinates of the line
coordinates = 100, 150, 550, 170

# Draw a dashed vertical line, 5px dash and 1px space
C1.create_line(coordinates, dash=(5, 1))
C1.pack()

win.mainloop()
