import tkinter  as tk

window = tk.Tk()

for i in range(3):
 for j in range(3):
    frame = tk.Frame(
        master = window,
        relief = tk.RAISED,
        borderwidth = 1
    )

    frame. grid(row =i,column =j,pady= 5)

    label = tk.Label(master=frame,text = f"row {i}\nColumn {j}")

    label.pack()

window.mainloop()



