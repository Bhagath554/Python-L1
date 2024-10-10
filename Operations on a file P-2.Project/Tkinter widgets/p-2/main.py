from tkinter import * 
from tkinter import messagebox

root = Tk()
root.geometry('200x200')


#message.boxsowwarning("window name", "Text to be Displayed")
def msg() :
        messagebox.showwarning("Alert", " Stop! Virus Found")
button = Button(root,text = "Search for virus",command = msg)

button.place(x=40,y=80)

root.mainloop()