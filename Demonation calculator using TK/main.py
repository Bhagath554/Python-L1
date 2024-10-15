from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

root = Tk()
root.title('Domination Calculator')
root.configure(bg='lightblue')
root.geometry('650x400')



image = PhotoImage(file="-lo.png")
label.place(x=140 , y= 20)


label1 = Label(root,text='Hello Welcome to The Domination Calculator',bg = 'lightblue')
label1.place(relx = '0.5',y=340,anchor=Center)







def msg():
    MsgBox = messagebox.showinfo(
        "Alert","Do you want to Calculate the denomation count ?")
       
    if MsgBox == 'ok' :
        topwin()

Button1 = Button(root,
                 text = "Let's get Started.",
                 command=msg,
                 bg = 'Brown',
                 fg = 'White'
                 )

Button1.place(x='260',y='360')

def topwin():
    top = Toplevel()
    top.title('Denomation Calculator')
    top.configure(bg = 'orange')
    top.geometry("650x350=50=50")

    label = Label(top,text='Enter the Amount',bg='light grey')
    entry = Entry(top)
    lbl = Label(top,text='Here Are the notes for the Entered Amount',bg='light grey')

    l1 = Label(top,text='2000',bg='lightgrey')
    l2 = Label(top,text='500',bg='lightgrey')
    l3 = Label(top,text='100',bg='lightgrey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator() :
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
           
            t1.delete(0, End)
            t2.delete(0, End)
            t3.delete(0, End)

            t1.insert(END,str(note2000))
            t3.insert(END,str(note500))
            t1.insert(END,str(note100))
        except ValueError :
            messagebox.showerror('Please Enter a Valid Number')

    btn = Button(top,text = 'Calculate',command=calculator,bg = 'Brown',fg='White')
     

    label.place(x=230, y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place(x=140,y=170)

    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l1.place(x=180,y=260)

    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)


top.mainloop()



root.mainloop()





    