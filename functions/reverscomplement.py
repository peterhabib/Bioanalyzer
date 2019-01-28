from Bio.Seq import Seq
from Bio import SeqIO
from tkinter import filedialog
from tkinter import *
import tkinter as tk
def revcom():
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
        namein = filedialog.asksaveasfilename(parent=win)
        e2.insert(END, namein)
        print(e2.get())

    def out():
        infile = e1.get()
        outfile = e2.get()

        try:
            for record in SeqIO.parse(str(infile), "fasta"):
                print(">%s" % record.id)
                coding_dna = Seq("%s" % record.seq)
                templatedna = coding_dna.reverse_complement()

                trc = ">%s\n\n" % templatedna.reverse_complement().transcribe()
                print(trc)
        except FileNotFoundError:
            return

        with open(outfile, "w") as f:
            for record in SeqIO.parse(str(infile), "fasta"):
                print(">%s" % record.id)
                coding_dna = Seq("%s" % record.seq)
                templatedna = coding_dna

                transc = templatedna.reverse_complement()
                f.write(str(">%s\n%s\n\n" % (record.id, transc)))

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



#revcom()