from tkinter import * 
import time 


#Random Quote
p=open("lotus.txt","r", encoding="utf8")
l=p.readlines()
j=[]

for i in range(len(l)):
    if i%2==0:
        j.append(l[i])

import random as rd

def qg():
    global j
    ind=rd.randint(0,50)
    
    d=[j[ind]]
    d=d[0].split(" ")
    q=d[1:-2]
    quote=""
    for i in q:
        quote+=i+" "
    a=str(d[-2])+" "+str(d[-1])
    c=quote+"\n\n"+a
    
    return c

# CREATING A SPLASH WINDOW WHICH LASTS FOR SOME TIME
splash_root = Tk()
splash_root.title("DAY BUDDY!!")   # Defines the title of the  UI Window
splash_root.geometry('1000x1000')   # Assigns the size of the window
 
splash_label1 = Label(splash_root, text = 'Welcome to', font=('sens serif', 35), bg='black', fg = 'black')  # Creates a label for the window
splash_label1.pack()
splash_root['bg'] = 'black'
# PROCEDURE FOR ADDING THE LOGO TO THE SPLASH SCREEN
photo = PhotoImage(file='daybuddylogo.png')  # THIS  CREATES AN IMAGE AND ASSIGNS IT TO A VARIABLE
photo_label = Label(image=photo)  # THIS WILL SHOW THE IMAGE AS A LABEL
photo_label.pack()

import time

# CREATING A SECOND WINDOW WHICH WILL COME LATER
def main_window():
    splash_root.destroy()
    root = Tk()   # DEFINING THE WINDOW
    # SPECIFICATIONS OF WINDOW
    root.title('main')
    root.geometry('1055x4450')
    root.resizable(False,False)
    root['bg'] = 'black'

   # PRINTING THE LOGO AS A LABEL
    photo = PhotoImage(file='daybuddylogo.png')  # THIS  CREATES AN IMAGE AND ASSIGNS IT TO A VARIABLE
    photo_label = Label(image=photo)  # THIS WILL SHOW THE IMAGE AS A LABEL
    photo_label.image = photo
    photo_label.grid(row=0, column=1, rowspan=3)

    display_quote = Label(root,
                          height=7,
                          pady=10,
                          wraplength=700,
                          font=("Times", 15, "bold"),
                          bg="#f72545"
                          )
    def qgenerate():
        display_quote.configure(text=str(qg()), fg="Green", font=("Playfair", 15), bg="Black")

    display_quote.grid(row=3, column=0, stick="WE", padx=28, pady=15, columnspan=3)
    buttonQ=Button(text="Generate Quote",command=qgenerate,bg="#2718c9",font="Times",fg="White",activebackground="#6b0e63",activeforeground="White")
    buttonQ.grid(row=4,column=1,stick="WE",padx=28,pady=10)
    # DEFINING BUTTONS
    
    def dday():
        from datetime import datetime
        import tkinter as tk

        # Function to calculate the number of days between two dates
        def calculate_d_days(today, date2):
            delta = date2 - today
            return delta.days

        # Function to update the D-Day label when the button is clicked
        def update_d_day():
                # Get the dates from the entry widgets
        
            date2_str = date2_entry.get()

            # Convert the dates to datetime objects
            today = datetime.today().date()
            date2 = datetime.strptime(date2_str, '%Y-%m-%d').date()

            # Calculate the number of days between the two dates
            d_days = calculate_d_days(today, date2)

            # Update the label with the result
            d_day_label.config(text=f'{d_days} days to go!')

        # Create the main window
        root = tk.Tk()
        root.title("D-Day Calendar")
        root.geometry('700x500')

        # Create the date entry widgets
        date1_label = tk.Label(root, text="TODAY'S DATE:")
        date1_label.pack()
        today = datetime.today().strftime('%Y-%m-%d')
        today_label = tk.Label(root, text=today)
        today_label.pack()
        date2_label = tk.Label(root, text="TARGET DATE:")
        date2_label.pack()
        date2_entry = tk.Entry(root)
        date2_entry.pack()

        # Create the calculate button
        calculate_button = tk.Button(root, text="Calculate D-Days", command=lambda:[update_d_day(),qgenerate()])
        calculate_button.pack()

        # Create the D-Day label
        d_day_label = tk.Label(root, text="D-Days:")
        d_day_label.pack()

        # Run the main loop
        root.mainloop()
    
    btn1 = Button(root, text = 'D-DAY', bg = 'orange', fg = 'black', padx = 100, pady = 30, command=dday)
    btn1.grid(row = 0, column=0)
    
    def todo():
        from tkinter import messagebox

        def newTask():
            task = my_entry.get()
            if task != "":
                lb.insert(END, task)
                my_entry.delete(0, "end")
            else:
                messagebox.showwarning("warning", "Please enter some task.")

        def deleteTask():
            lb.delete(ANCHOR)
    
        ws = Tk()
        ws.geometry('500x450+500+200')
        ws.title('Todo_List')
        ws.config(bg='#223441')
        ws.resizable(width=False, height=False)

        frame = Frame(ws)
        frame.pack(pady=10)

        lb = Listbox(
            frame,
            width=25,
            height=8,
            font=('Times', 18),
            bd=0,
            fg='#464646',
            highlightthickness=0,
            selectbackground='#a6a6a6',
            activestyle="none",
    
        )
        lb.pack(side=LEFT, fill=BOTH)

        task_list = [
            'Breakfast',
            'Exercise',
            'CSET101 Lab',
            'EMAT101L Tutorial',
            'CSET 102 Lecture',
            'Lunch',
            'EMAT assignment',
            'Snacks'
            ]

        for item in task_list:
            lb.insert(END, item)

        sb = Scrollbar(frame)
        sb.pack(side=RIGHT, fill=BOTH)

        lb.config(yscrollcommand=sb.set)
        sb.config(command=lb.yview)

        my_entry = Entry(
            ws,
            font=('times', 24)
            )

        my_entry.pack(pady=20)

        button_frame = Frame(ws)
        button_frame.pack(pady=20)

        addTask_btn = Button(
            button_frame,
            text='Add Task',
            font=('times 14'),
            bg='#c5f776',
            padx=20,
            pady=10,
            command=newTask
        )
        addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

        delTask_btn = Button(
            button_frame,
            text='Delete Task',
            font=('times 14'),
            bg='#ff8b61',
            padx=20,
            pady=10,
            command=deleteTask
        )
        delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


        ws.mainloop()
    btn2 = Button(root, text = 'ToDo LIST', bg = 'yellow', fg = 'black', padx = 92, pady = 30, command=lambda:[todo(),qgenerate()])
    btn2.grid(row=1,column=0)

    def time_table():
        import tkinter as tk
        import datetime

        # Create the table
        root1 = tk.Tk()
        root1.title("Timetable")

        def calculate_time():
            # hours entered by the user
            hours = eval(sleep.get())
            if float(hours) > 9:
                # excess sleep
                bedtime['text'] = ("Try reducing your sleep hours")

            elif float(hours) <= 3:
                # less sleep
                bedtime['text'] = ("Sleep time too low, Not Healthy!")

            elif not hours:
                # Invalid
                bedtime['text'] = ("Please enter a numeric value")

            else:
                # Create a datetime object for 3 AM
                time = datetime.datetime(2020, 1, 1, 3, 0, 0)

                # Subtract the specified number of hours from the time
                downtime = time - datetime.timedelta(hours=hours) / 2
                uptime = time + datetime.timedelta(hours=hours) / 2

                # Display the resulting time
                bedtime['text'] = "You Should sleep from: {} to {}".format(downtime.strftime("%I:%M %p"),
                                                                           uptime.strftime("%I:%M %p"))
                frame = tk.Frame(root1)
                frame.grid(row=6, column=0, sticky="nsew")

                # Defining timestamps and time variables
                mrng_study = uptime + datetime.timedelta(minutes=30)
                dinner = downtime - datetime.timedelta(hours=2)
                dinner_time = "{} to {}".format((dinner - datetime.timedelta(minutes=30)).strftime("%I:%M %p"),
                                                dinner.strftime("%I:%M %p"))

                if dinner.hour == 10:
                    dinner_time: "09:30 PM to 10:00 PM"
                else:
                    dinner_time = dinner_time

                if mrng_study.hour >= 8:
                    mrng = 'No morning study time,'
                    time = 'Go to Breakfast then Lectures'
                else:
                    mrng = 'Available Morning Study time:'
                    time = mrng_study.strftime("%I:%M %p") + " to 08:00 AM"

                if yes_no.get():
                    eve = " 1hr of Gym/Sports + 15 minutes buffer"
                else:
                    eve = "1hr of Leisure time/Rest + 15 minutes buffer"
                # defining timetable list
                timetable = [
                    (mrng, time),
                    ("Breakfast:", "till 08:25 AM"),
                    ("Morning Classes:", "till 11:40"),
                    ("Lunch:", "25mins"),
                    ("Afternoon Classes:", "till 05:30 PM"),
                    ("Snacks:", "for 15 min till 06:00 PM"),
                    (eve, ""),
                    ("Available Evening study time:",
                     "07:15 to {}".format((dinner - datetime.timedelta(minutes=45)).strftime("%I:%M %p"))),
                    ("Dinner from:", dinner_time),
                    ("15 min break", ""),
                    ("Available Night Study time:",
                     "till {}".format((downtime - datetime.timedelta(minutes=15)).strftime("%I:%M %p")))
                ]

                # Displaying timetable list
                def update_table():
                    for i, row in enumerate(timetable):
                        subject_label = tk.Label(frame, text=row[0], padx=5, pady=5)
                        subject_label.grid(row=i, column=0, sticky="w")
                        time_label = tk.Label(frame, text=row[1], padx=5, pady=5)
                        time_label.grid(row=i, column=1, sticky="w")

                frame.columnconfigure(0, weight=1)
                frame.columnconfigure(1, weight=1)

                update_table()

        # Defining Labels and Entries
        label = tk.Label(root1, text="Enter Hours of sleep:", fg="black")
        sleep = tk.Entry(root1, fg="green", borderwidth=10)

        label2 = tk.Label(root1, text="Sports/Gym:", fg="black")
        yes_no = tk.BooleanVar()
        act = tk.Checkbutton(root1, text="Yes", variable=yes_no)
        bedtime = tk.Label(root1, text='')

        emptylabel = tk.Label(root1, text='')

        # Defining button
        buttonCal = tk.Button(root1, text="Ok", command=calculate_time).grid(row=3, column=0)

        # Displaying everything
        label.grid(row=0, column=0)
        sleep.grid(row=0, column=1)
        label2.grid(row=2, column=0)
        act.grid(row=2, column=1)
        bedtime.grid(row=5, column=0)
        emptylabel.grid(row=4, column=0)
        root1.mainloop()

    btn3 = Button(root, text = 'TIME TABLE',bg = 'indigo', fg = 'black', padx = 87, pady = 30, command =lambda:[time_table(),qgenerate()])
    btn3.grid(row=2,column=0)

    def count():
        import tkinter as tk
        import tkinter.messagebox
        import time
        from playsound import playsound  

        class Application(tk.Frame): 
            def __init__(self, master, *args, **kwargs):
                tk.Frame.__init__(self, master, *args, **kwargs)
                self.master = master
                self.running = False
                self.time = 0
                self.hours = 0
                self.mins = 0
                self.secs = 0
                self.build_interface()

            def build_interface(self):
                self.time_entry = tk.Entry(self)
                self.time_entry.grid(row=0, column=1)

                self.clock = tk.Label(self, text="00:00:00", font=("Courier", 20), width=10)
                self.clock.grid(row=1, column=1, stick="S")

                self.time_label = tk.Label(self, text="hour   min   sec", font=("Courier", 10), width=15)
                self.time_label.grid(row=2, column=1, sticky="N")

                self.power_button = tk.Button(self, text="Start", command=lambda: self.start())
                self.power_button.grid(row=3, column=0, sticky="NE")

                self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
                self.reset_button.grid(row=3, column=1, sticky="NW")

                self.quit_button = tk.Button(self, text="Quit", command=lambda: self.quit())
                self.quit_button.grid(row=3, column=3, sticky="NE")

                self.pause_button = tk.Button(self, text="Pause", command=lambda: self.pause())
                self.pause_button.grid(row = 3,column=2, sticky = "NW")

                self.master.bind("<Return>", lambda x: self.start())
                self.time_entry.bind("<Key>", lambda v: self.update())

            def calculate(self):
                """time calculation"""
                self.hours = self.time // 3600
                self.mins = (self.time // 60) % 60
                self.secs = self.time % 60
                return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

            def update(self):
                """validation"""
                self.time = int(self.time_entry.get())
                try:
                    self.clock.configure(text=self.calculate())
                except:
                    self.clock.configure(text="00:00:00")

            def timer(self):
                """display time"""
                if self.running:
                    if self.time <= 0:
                        playsound("micro2.wav")
                        self.clock.configure(text="Time's up!")
                    else:
                        self.clock.configure(text=self.calculate())
                        self.time -= 1
                        self.after(1000, self.timer)

            def start(self):
                """start timer"""
                try:
                    self.time = int(self.time_entry.get())
                    self.time_entry.delete(0, 'end')
                except:
                    self.time = self.time
                self.power_button.configure(text="Stop", command=lambda: self.stop())
                self.master.bind("<Return>", lambda x: self.stop())
                self.running = True
                self.timer()

            def stop(self):
                """Stop timer"""
                self.power_button.configure(text="Start", command=lambda: self.start())
                self.master.bind("<Return>", lambda x: self.start())
                self.running = False

            def reset(self):
                """Resets the timer to 0."""
                self.power_button.configure(text="Start", command=lambda: self.start())
                self.master.bind("<Return>", lambda x: self.start())
                self.running = False
                self.time = 0
                self.clock["text"] = "00:00:00"

            def quit(self):
                """quit the window"""
                if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
                    root.destroy()

            def pause(self):
                """Pause timer"""
                self.pause_button.configure(text="Resume", command=lambda: self.resume())
                self.master.bind("<Return>", lambda x: self.resume())
                if self.running == True:
                    self.running = False
                self.timer()
               
            def resume(self):
                """Resume timer"""
                self.pause_button.configure(text="Pause", command=lambda: self.pause())
                self.master.bind("<Return>", lambda x: self.pause())
                if self.running == False:
                    self.running = True
                self.timer()
                

            


        if __name__ == "__main__":
            """Main loop of timer"""
            root = tk.Tk()
            root.title("TIMER")
            Application(root).pack(side="top", fill="both", expand=True)
            root.mainloop()
    
    
    
    btn4 = Button(root, text = 'COUNTDOWN', bg = 'purple', fg = 'black', padx = 79, pady = 30, command=lambda:[count(),qgenerate()])
    btn4.grid(row=2,column=2)

    import webview as wb
    def sy():
        wb.create_window("spotify",'https://www.spotify.com/')
        wb.start()

    btn5 = Button(root, text = 'SPOTIFY', bg = 'green', fg = 'black', padx = 94, pady = 30, command=lambda:[sy(),qgenerate()])
    btn5.grid(row=1,column=2)

    def yt():
        wb.create_window("youtube",'https://youtube.com')
        wb.start()
    btn6 = Button(root, text = 'YOUTUBE', bg = 'red', fg = 'black', padx =91, pady =30, command=lambda:[yt(),qgenerate()])
    btn6.grid(row=0,column=2)


# FIXING THE TIME OF THE SPLASH WINDOW
splash_label1.after(1000, main_window)    #TIME IS SET IN MILLISECONDS



mainloop()   # TKINTER MAINLOOP
