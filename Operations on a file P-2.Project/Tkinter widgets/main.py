from tkinter import *
from PIL import image , imageTK

root = tk()

root,title('Image')
root.geometry('300x500')
upload = image.open("download.jpeg")

image = tkinter.PhotoImage(upload)

label = Label(root,image=image,height=350,width=300)
label.place(x=50,y=0)
label12 = Label(root,tex="This is how you add Image in Tkinter")

label12.place(x=40,y=360)

root.mainloop()