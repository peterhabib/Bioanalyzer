from tkinter import *
from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
import os
import tkinter
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from Bio import SeqIO
def opf(tableget , lenget):
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
        table = tableget
        min_pro_len = lenget
        fasta = open("result.fasta", "w")
        with open(outfile, "w") as f:
            ides = open(infile).readlines()
            for line in ides:
                ln = line
                print(line)
                Entrez.email = "your.email@helsinki.fi"
                handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id=line)
                record = handle.read()
                fasta.write(str(record))
            for record in SeqIO.parse("result.fasta", "fasta"):
                ids = record.id
                for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:
                    for frame in range(3):
                        length = 3 * ((len(record) - frame) // 3)
                        for pro in nuc[frame:frame + length].translate(table).split("*"):
                            if len(pro) >= int(min_pro_len):
                                print("%s  - length %i, strand %i, frame %i" % (pro[0:], len(pro), strand, frame))
                                o = "ID:%s\n%s\nlength %i, \nstrand %i,\nframe %i\n\n" % (
                                    ids, pro[0:], len(pro), strand, frame)
                                f.write("%s\n\n" % o)




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

#opf("Standard" , "10")