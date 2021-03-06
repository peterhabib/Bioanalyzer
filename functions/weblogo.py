from tkinter import filedialog
from tkinter import *
import tkinter as tk
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import motifs
def weblogo(lens):
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    Label(win, text="Input File").grid(row=0)
  

    e1 = Entry(win, textvariable=sv1)
   

    e1.grid(row=0, column=1)
  

    def inpo1():
        namein = filedialog.askopenfilename(parent=win)
        e1.insert(END, namein)
        print(e1.get())


    def out():
        infile = e1.get()


        list2 = []
        for record in SeqIO.parse(str(infile), "fasta"):
            list2.append(record.seq[0:int(lens)])
        m = motifs.create(list2)



        win.destroy()



    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()
