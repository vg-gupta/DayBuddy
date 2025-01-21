#opening .txt file containing quotes
f=open("lotus.txt","r")
lof=f.readlines()
j=[]
#eliminating break line character "\n"
for i in range(len(lof)):
    if i%2==0:
        j.append(lof[i])
print("Total quotes:",len(j)) #prints total no:of quotes
#importing random module for quote selection
import random as rd
#random quote generating function
def qg():
    global j
    ind=rd.randint(0,50)
    print(ind)
    d=[j[ind]]
    d=d[0].split(" ")
    q=d[1:-2]
    quote=""
    for i in q:
        quote+=i+" "
    a=str(d[-2])+" "+str(d[-1])
    c=quote+"\n\n"+a
    print("Quote: ",quote," Author: -",a,sep="")
    return c

#GUI
#creating the tkinter window to display quotes
from tkinter import*
root=Tk()
root.geometry("900x300")
root.title("Random Quote Generator")
root.grid_columnconfigure(0, weight=1)
root.configure(bg="#b2d6d6")
#Label bg color selection
def colorz():
    color=rd.choice(["#fcba03","#36e0e0","#b543bf","#f72545"])
    return color
#label to diplay quotes
display_quote=Label(root,text="Press the button below",                    
                    height=7,
                    pady=10,
                    wraplength=700,
                    font=("Times",15,"bold"),
                    bg="#f72545"
                     )
display_quote.grid(row=0,column=0,stick="WE",padx=28,pady=15)
#Label fontstyle selection
def fontz():
    font=rd.choice(["Chiller","Times","Impact","Aerial","Lato","Helvetica"])
    return font
#Label bg and font style change 
def qgenerate():
    display_quote.configure(text=str(qg()),fg="Black",font=fontz(),bg=colorz())
#button to generate quotes
button=Button(text="Generate Quote",command=qgenerate,bg="#2718c9",font="Times",fg="White",activebackground="#6b0e63",activeforeground="White")
button.grid(row=1,column=0,stick="WE",padx=28,pady=10)
#loop to keep the tkinter window open
root.mainloop()
