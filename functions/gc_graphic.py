from Bio import SeqIO
from Bio.SeqUtils import GC
from tkinter import filedialog
from tkinter import *
import tkinter as tk
def gcsgraph():
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
        gc_values = sorted(GC(rec.seq) for rec in SeqIO.parse(str(infile), "fasta"))
        import pylab
        pylab.plot(gc_values)
        pylab.title("%i orchid sequences\nGC%% %0.1f to %0.1f" % (len(gc_values), min(gc_values), max(gc_values)))
        pylab.xlabel("Genes")
        pylab.ylabel("GC%")
        pylab.show()

        win.destroy()

    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()


