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
    Label(win, text="Output Result").grid(row=1)
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
        namein = filedialog.asksaveasfilename(parent=win)
        e2.insert(END, namein)
        print(e2.get())

    def out():
        lb.configure(text="LOADING....", font=('Times Roman', 15, 'bold'))
        lb.update()
        file1 = open("result.fasta", "w")
        Entrez.email = "your.email@helsinki.com"
        file = open(e1.get(), "r")
        for line in file:
            handle = Entrez.efetch(db="%s" % database, rettype="%s"%type, retmode="text", id=line)
            record = handle.read()
            print(record)
            file1.write(record)

        filename = e2.get()
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        fread = open("result.fasta", "r")
        fr = fread.read()
        file = open(filename, "w")
        records = SeqIO.parse("result.fasta", "fasta")
        for record in records:
            print(record)
            print("")
            print("")
            filenamess = record.name + ".fasta"
            fasta = "ID: %s\nName: %s\nNumber of features: %s\nSequence: %s\n\n" % (
                record.id, record.name, record.description, record.seq)
            recordid = open(filenamess, "w")

            recordid.write(str(fasta))
        os.remove("result.fasta")
        file.write(fr)
        file.close()
        lb.configure(text="Process Completed", font=('Times Roman', 15, 'bold'))
        lb.update()
        time.sleep(2)

        win.quit()

    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()



