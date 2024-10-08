from tkinter import *

window = Tk()

window.title('Tkinter Sample')
window.geometry('350x350')

greeting = Label(text = "Hello User", fg = 'yellow',bg = 'black')
button = Button(text = "Click Me",fg = 'orange',bg = 'red')
entry = Entry(fg = 'red',bg = 'green')
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master = window, relief = RAISED, borderwidth = 5)
frame.pack()

label = Label(master=frame,text = 'Sample Frame')

label.pack()

textbox = Text(fg= 'green',bg = 'red')

textbox.pack()

window.mainloop()
