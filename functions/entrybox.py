from tkinter import *

def show():
    print(e1.get())
    return e1.get()
    master.destroy()




master = Tk()
Label(master, text="First Name").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show).grid(row=3, column=1, sticky=W, pady=4)
master.mainloop()


