from Bio import Entrez
from Bio import SeqIO
from tkinter import filedialog
import os
import errno
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import time

label = {}
label = ""




def download(database , type):
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    Label(win, text="ID List").grid(row=0)
    Label(win, text="Choose Output Directory").grid(row=1)
    lb = Label(win, text=label)
    lb.grid(row=3)

    e1 = Entry(win, textvariable=sv1)
    e2 = Entry(win, textvariable=sv2)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    def inpo1():
        namein = filedialog.askopenfilename(parent=win)
        e1.insert(END, namein)
        print(e1.get())

    def inpo2():
        namein = filedialog.askdirectory(parent=win)
        e2.insert(END, namein)
        print(e2.get())

    def out():
        
        lb.configure(text="LOADING....", font=('Times Roman', 15, 'bold'))
        lb.update()
        Entrez.email = "your.email@helsinki.com"
        file = open(e1.get(), "r")
        for i,line in enumerate(file):
            handle = Entrez.efetch(db="%s" % database, rettype="%s"%type, retmode="text", id=line)
            record = handle.read()
            print(record)

            completename =e2.get()+"/ "+str(line)+".txt"
            if not os.path.exists(os.path.dirname(completename)):
                try:
                    os.makedirs(os.path.dirname(completename))
                except IOError:
                    pass
            file1 = open("%s"%completename , 'w')
            file1.write(record)





        lb.configure(text="Process Completed", font=('Times Roman', 15, 'bold'))
        lb.update()
        time.sleep(2)

        win.quit()

    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()



