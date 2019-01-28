from Bio import Phylo
from Bio import SeqIO
import networkx, pylab
import pylab
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
import tkinter as tk
from tkinter import *
from tkinter import filedialog


def phylotree():
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
        namein = filedialog.askopenfilename(parent=win)
        e2.insert(END, namein)
        print(e2.get())

    def out():
        records = SeqIO.parse(e1.get(), "fasta")

        lens = []

        for record in records:
            print(record.seq)
            ids = record.id
            sequence = record.seq
            op = lens.append(record.id)
            # print(lens)

        lengthmax = len(max(lens, key=len))
        lengthmin = len(min(lens, key=len))
        line = "  %s             %s\n" % (len(lens), "125")
        file = open("phylo.phy", "w")
        file.write(line)

        for i, id in enumerate(lens):
            if lengthmin < int(lengthmax):
                add = int(lengthmax) - int(len(id))
                # print(i)
                id = id + (add * "-")
                id = id.replace(".", "")
                id = id.replace("_", "")
                to_be_write = "%s%s%s    %s" % (i, "-", id, sequence[0:100])
                # file.write("  %s                    %s\n"%(num_rec,seqlen))
                file.writelines(str("%s\n" % to_be_write))
                print(id)


            else:
                add = int(lengthmax) - int(len(id))
                id = id + (add * "-")
                id = id.replace(".", "")
                id = id.replace("_", "")
                to_be_write = "%s    %s" % (id, sequence[0:100])
                # file.write("  %s                    %s\n"%(num_rec,seqlen))

                file.writelines(str("%s\n" % (to_be_write)))
                print(id)

        # Read the sequences and align
        aln = AlignIO.read('/home/peter/Desktop/Moduls/phylogenetic tree/phylo.phy', 'phylip')

        # Print the alignment
        print(aln)

        # Calculate the distance matrix
        calculator = DistanceCalculator('identity')
        dm = calculator.get_distance(aln)

        # Print the distance Matrix
        print('\nDistance Matrix\n===================')
        print(dm)

        # Construct the phylogenetic tree using UPGMA algorithm
        constructor = DistanceTreeConstructor()
        tree = constructor.upgma(dm)

        # Draw the phylogenetic tree
        Phylo.draw(tree)

        # Print the phylogenetic tree in the terminal
        print('\nPhylogenetic Tree\n===================')
        Phylo.draw_ascii(tree)

        win.destroy()

    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()

