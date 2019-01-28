from Bio import SeqIO
from Bio.SeqUtils import GC
from tkinter import filedialog
from tkinter import *
import tkinter as tk

def gccontent():
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    Label(win, text="Input File").grid(row=0)
    Label(win, text="Output File").grid(row=1)

    e1 = Entry(win, textvariable=sv1)
    e2 = Entry(win, textvariable=sv2)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    def inpo1():
        namein = filedialog.askopenfilename(parent=win)
        e1.insert(END, namein)
        print(e1.get())

    def inpo2():
        namein = filedialog.asksaveasfilename(parent =win)
        e2.insert(END, namein)
        print(e2.get())

    def out():
        inputfile = e1.get()
        outfile = e2.get()
        try:
            for record in SeqIO.parse(str(inputfile), "fasta"):
                seq = record.seq
                gc = GC(seq)
                id = record.id
                print("Record ID:%s\nSequence:%s\nGC Content:%s\n" % (id, seq, gc))
        except FileNotFoundError:
            return

        with open(outfile, "w") as f:
            for record in SeqIO.parse(str(inputfile), "fasta"):
                seq = record.seq
                gc = GC(seq)
                id = record.id
                res = ">%s\n%s\nGC:%s\n\n" % (id, seq, gc)
                f.write(res)



        r = open(e2.get(), 'r').read()
        root = Tk()
        S = Scrollbar(root)
        T = Text(root, height=50, width=500)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        S.config(command=T.xview)
        T.config(yscrollcommand=S.set)
        T.config(xscrollcommand=S.set)
        quote = r
        T.insert(END, quote, 'color')
        mainloop()

    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()



