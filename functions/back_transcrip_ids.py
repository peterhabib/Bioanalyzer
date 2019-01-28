from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk
def bacsids():
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
            ides = open(infile)


        except FileNotFoundError:
            print("Error")

        fasta = open("result.fasta", "w")
        result = open(outfile, "w")
        if 1 == 1:
            for line in ides:
                ln = line
                Entrez.email = "your.email@helsinki.fi"
                handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id=ln)
                record = handle.read()
                fasta.write(str(record))
            for record in SeqIO.parse("result.fasta", "fasta"):
                # print(record.id)
                # print(record.seq)
                accs = record.id
                coding_dna = Seq("%s" % record.seq)
                templatedna = coding_dna.reverse_complement().back_transcribe()
                trc = ">%s" % templatedna
                result.write(str(">%s\n%s\n\n" % (accs, trc)))

        if os.path.exists("result.fasta"):
            os.remove("result.fasta")
        else:
            print("")

        result.close()
        fasta.close()



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
