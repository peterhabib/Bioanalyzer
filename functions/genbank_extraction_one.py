from Bio import SeqIO

from tkinter import filedialog
from tkinter import *
import tkinter as tk
def onegbk():

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
            for rec in SeqIO.parse(infile, "genbank"):
                if rec.features:
                    for feature in rec.features:
                        if feature.type == "CDS":
                            print(feature.location)
                            print(feature.qualifiers["protein_id"])
                            print(feature.location.extract(rec).seq)
                            print(rec.description)
                            print(rec.seq)
                            print(rec.id)
        except FileNotFoundError:
            return

        with open(outfile, "w") as f:
            for rec in SeqIO.parse(infile, "genbank"):
                if rec.features:
                    for feature in rec.features:
                        if feature.type == "CDS":
                            id = (feature.qualifiers["protein_id"])
                            gene = (feature.qualifiers["gene"])
                            codon = (feature.qualifiers["codon_start"])
                            Trans = (feature.qualifiers["transl_table"])
                            prod = (feature.qualifiers["product"])
                            transl = (feature.qualifiers["translation"])

                            trc = "Protein ID: %s\nGene: %s\nCodon Start: %s\nTransaltion Table: %s\nProduct: %s\nTranslation: %s\n\n" % (
                            id, gene, codon, Trans, prod, transl)
                            f.write(str(trc))

        win.destroy()

    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()








