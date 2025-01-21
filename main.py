from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Day Buddy")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text="Select one\n")
lbl.grid()

# function to display text when
# button is clicked
def clicked():
    import CountdownTkinter

# button widget with red color text
# inside
btn = Button(root, text="CountDown",
             fg="red", command=clicked)
# set Button grid
btn.grid(column=1, row=1)

# function to display text when
# button is clicked
def clicked1():
    import ToDo

# button widget with red color text
# inside
btn = Button(root, text="ToDo List",
             fg="red", command=clicked1)
# set Button grid
btn.grid(column=2, row=1)

# Execute Tkinter
root.mainloop()
