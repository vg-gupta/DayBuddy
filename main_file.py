from tkinter import * 

# CREATING A SPLASH WINDOW WHICH LASTS FOR SOME TIME
splash_root = Tk()
splash_root.title("DAY BUDDY!!")   # Defines the title of the  UI Window
splash_root.geometry('1920x1080')   # Assigns the size of the window
 

splash_label1 = Label(splash_root, text = 'Welcome to', font=('sens serif', 35), bg='black', fg = 'black')  # Creattes a label for the window
splash_label1.pack()
splash_root['bg'] = 'black'
# PROCEDURE FOR ADDING THE LOGO TO THE SPLASH SCREEN
photo = PhotoImage(file='daybuddylogo.png')  # THIS  CREATES AN IMAGE AND ASSIGNS IT TO A VARIABLE
photo_label = Label(image=photo)  # THIS WILL SHOW THE IMAGE AS A LABEL
photo_label.pack()


# CREATING A SECOND WINDOW WHICH WILL COME LATER
def main_window():
    splash_root.destroy()



    # main = Tk()
    # main.geometry('1920x1080')
    # main.title('Main Window')  # Defines the title of the main window
    # # main_label1 = Label(main, text='MAIN SCREEN', font=('algerian', 50))
    # main['bg'] = 'black'   # BACKGROUND COLOR OF MAIN WINDOW WILL BE BLACK
    # # main_label1.pack()
    root = Tk()   # DEFINING THE WINDOW
    # SPECIFICATIONS OF WINDOW
    root.title('main')
    root.geometry('1920x1080')
    root['bg'] = 'black'

    # PRINNTING THE LOGO AS A LABEL
    img = PhotoImage(file='daybuddylogo.png')
    photo_label2 = Label(image=img)
    photo_label2.pack()


    # DEFINING BUTTONS
    btn1 = Button(root, text = 'CALENDAR', bg = 'orange', fg = 'black', padx = 92, pady = 30)
    btn1.pack(side = 'left')

    btn2 = Button(root, text = 'ToDo LIST', bg = 'yellow', fg = 'black', padx = 92, pady = 30)
    btn2.pack(side = 'left')

    btn3 = Button(root, text = 'TIME TABLE',bg = 'indigo', fg = 'black', padx = 92, pady = 30)
    btn3.pack(side = 'left')

    btn4 = Button(root, text = 'COUNTDOWN', bg = 'purple', fg = 'black', padx = 92, pady = 30)
    btn4.pack(side = 'left')

    btn5 = Button(root, text = 'SPOTIFY', bg = 'green', fg = 'black', padx = 92, pady = 30)
    btn5.pack(side = 'left')

    btn6 = Button(root, text = 'YOUTUBE', bg = 'red', fg = 'black', padx =92, pady =30)
    btn6.pack(side = 'left')
    

# FIXING THE TIME OF THE SPLASH WINDOW
splash_label1.after(2000, main_window)    #TIME IS SET IN MILLISECONDS

mainloop()   # TKINTER MAINLOOP
