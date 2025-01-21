
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


from tkinter import*
root=Tk()
root.geometry("900x300")
root.title("Random Quote Generator")
root["bg"]="black"
root.grid_columnconfigure(0, weight=1)
root.configure(bg="#b2d6d6")

def colorz():
    color=rd.choice(["#fcba03","#36e0e0","#b543bf","#f72545"])
    return color

display_quote=Label(root, text="Press the button below",                    
                    height=7,
                    pady=10,
                    wraplength=700,
                    font=("Times",15,"bold"),
                    bg="#f72545"
                     )
display_quote.grid(row=0,column=0,stick="WE",padx=28,pady=15)

def fontz():
    font=rd.choice(["Elephant","Times","Impact","Aerial","Lato","Helvetica"])
    return font

def qgenerate():
    display_quote.configure(text=str(qg()),fg="Black",font=fontz(),bg=colorz())

button=Button(text="Generate Quote",command=qgenerate,bg="#2718c9",font="Times",fg="White",activebackground="#6b0e63",activeforeground="White")
button.grid(row=1,column=0,stick="WE",padx=28,pady=10)

root.mainloop()
