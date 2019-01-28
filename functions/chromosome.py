from reportlab.lib.units import cm
from Bio import SeqIO
from Bio.Graphics import BasicChromosome
from tkinter import filedialog
from tkinter import *
import tkinter as tk
def Chromsome(choice):
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    Label(win, text="Input GenBank File").grid(row=0)


    e1 = Entry(win, textvariable=sv1)


    e1.grid(row=0, column=1)


    def inpo1():
        namein = filedialog.askopenfilename(parent=win)
        e1.insert(END, namein)
        print(e1.get())


    def out():

        infile = e1.get()
        entries = [("Chromosome", infile)]

        max_len = 30432563  # Could compute this
        telomere_length = 1000000  # For illustration

        chr_diagram = BasicChromosome.Organism()
        chr_diagram.page_size = (200 * cm, 500 * cm)  # A4 landscape

        for index, (name, filename) in enumerate(entries):
            record = SeqIO.read(filename, "genbank")
            length = len(record)
            Radiochrom = choice
            if Radiochrom == "1":
                features = [f for f in record.features if f.type == "gene"]
            if Radiochrom == "2":
                features = [f for f in record.features if f.type == "trna"]
            if Radiochrom == "3":
                features = [f for f in record.features if f.type == "mrna"]
            # Record an Artemis style integer color in the feature's qualifiers,
            # 1 = Black, 2 = Red, 3 = Green, 4 = blue, 5 =cyan, 6 = purple
            for f in features: f.qualifiers["color"] = [index + 2]

            cur_chromosome = BasicChromosome.Chromosome(name)
            # Set the scale to the MAXIMUM length plus the two telomeres in bp,
            # want the same scale used on all five chromosomes so they can be
            # compared to each other
            cur_chromosome.scale_num = max_len + 2 * telomere_length

            # Add an opening telomere
            start = BasicChromosome.TelomereSegment()
            start.scale = telomere_length
            cur_chromosome.add(start)

            # Add a body - again using bp as the scale length here.
            body = BasicChromosome.AnnotatedChromosomeSegment(length, features)
            body.scale = length
            cur_chromosome.add(body)

            # Add a closing telomere
            end = BasicChromosome.TelomereSegment(inverted=True)
            end.scale = telomere_length
            cur_chromosome.add(end)

            # This chromosome is done
            chr_diagram.add(cur_chromosome)
            chr_diagram.draw("Chromosome.pdf", " ")
            print("done")

        win.destroy()

    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()