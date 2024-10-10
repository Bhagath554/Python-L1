from tkinter import * 

root = Tk()

root.geometry('400x300')
root.title("Main")

def topwin() :
       top = Toplevel()
       top.geometry('180x100')
       top.title("Toplevel")

       l2 = Label(root,text="This is Toplevel Window")

       l2.pack()

       top.mainloop()

l = Label(root,text="This is Root Window")
btn = Button(root,text= "Click Here to Open Anathor Window",command=topwin)
l.pack()
btn.pack()

root.mainloop()