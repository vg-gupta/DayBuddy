import tkinter as tk
import datetime

# Create the table
root = tk.Tk()
root.title("Timetable")
def calculate_time():
    #hours entered by the user
    hours = eval(sleep.get())
    if float(hours)>9:
        # excess sleep
        bedtime['text'] = ("Try reducing your sleep hours")
        
    elif float(hours)<=3:
        # less sleep
        bedtime['text'] = ("Sleep time too low, Not Healthy!")

    elif not hours:
        #Invalid
        bedtime['text'] = ("Please enter a numeric value")
        
    else:    
        # Create a datetime object for 3 AM
        time = datetime.datetime(2020, 1, 1, 3, 0, 0)
        
        # Subtract the specified number of hours from the time
        downtime = time - datetime.timedelta(hours=hours)/2
        uptime = time + datetime.timedelta(hours=hours)/2
        
        # Display the resulting time
        bedtime['text'] = "You Should sleep from: {} to {}".format(downtime.strftime("%I:%M %p"), uptime.strftime("%I:%M %p"))
        frame = tk.Frame(root)
        frame.grid(row=6, column=0, sticky="nsew")
        
        # Defining timestamps and time variables
        mrng_study = uptime + datetime.timedelta(minutes=30)
        dinner= downtime - datetime.timedelta(hours=2)
        dinner_time = "{} to {}".format((dinner - datetime.timedelta(minutes=30)).strftime("%I:%M %p"), dinner.strftime("%I:%M %p"))
        
        if dinner.hour == 10:
            dinner_time:"09:30 PM to 10:00 PM"
        else:
            dinner_time = dinner_time
            
        if mrng_study.hour >= 8:
            mrng = 'No morning study time,'
            time = 'Go to Breakfast then Lectures'    
        else:
            mrng = 'Available Morning Study time:'
            time = mrng_study.strftime("%I:%M %p")+" to 08:00 AM"
            
        if yes_no.get():
            eve = " 1hr of Gym/Sports + 15 minutes buffer"
        else:
            eve = "1hr of Leisure time/Rest + 15 minutes buffer"
        #defining timetable list    
        timetable = [
            (mrng, time),
            ("Breakfast:", "till 08:25 AM"),
            ("Morning Classes:", "till 11:40"),
            ("Lunch:", "25mins"),
            ("Afternoon Classes:", "till 05:30 PM"),
            ("Snacks:", "for 15 min till 06:00 PM"),
            (eve, ""),
            ("Available Evening study time:", "07:15 to {}".format((dinner - datetime.timedelta(minutes=45)).strftime("%I:%M %p"))),
            ("Dinner from:", dinner_time),
            ("15 min break", ""),
            ("Available Night Study time:", "till {}".format((downtime - datetime.timedelta(minutes=15)).strftime("%I:%M %p")))
        ]
        #Displaying timetable list
        def update_table():
            for i, row in enumerate(timetable):
                subject_label = tk.Label(frame, text=row[0], padx=5, pady=5)
                subject_label.grid(row=i, column=0, sticky="w")
                time_label = tk.Label(frame, text=row[1], padx=5, pady=5)
                time_label.grid(row=i, column=1, sticky="w")
    

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
    
        update_table()

#Defining Labels and Entries
label = tk.Label(text="Enter Hours of sleep:", fg="black")
sleep = tk.Entry(fg="green", borderwidth=10)

label2 = tk.Label(text="Sports/Gym:", fg="black")
yes_no = tk.BooleanVar()
act = tk.Checkbutton(root, text="Yes", variable=yes_no)
bedtime = tk.Label(root, text='')

emptylabel = tk.Label(root, text='')

#Defining button
buttonCal = tk.Button(root, text="Ok", command=calculate_time).grid(row=3, column=0)

#Displaying everything
label.grid(row=0, column=0)
sleep.grid(row=0, column=1)
label2.grid(row=2, column=0)
act.grid(row=2, column=1)
bedtime.grid(row=5, column=0)
emptylabel.grid(row=4, column=0)
root.mainloop()
