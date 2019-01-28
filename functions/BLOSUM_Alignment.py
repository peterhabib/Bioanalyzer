from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat.MatrixInfo import blosum100
from Bio.SubsMat.MatrixInfo import blosum95
from Bio.SubsMat.MatrixInfo import blosum90
from Bio.SubsMat.MatrixInfo import blosum85
from Bio.SubsMat.MatrixInfo import blosum80
from Bio.SubsMat.MatrixInfo import blosum75
from Bio.SubsMat.MatrixInfo import blosum70
from Bio.SubsMat.MatrixInfo import blosum65
from Bio.SubsMat.MatrixInfo import blosum62
from Bio.SubsMat.MatrixInfo import blosum60
from Bio.SubsMat.MatrixInfo import blosum55
from Bio.SubsMat.MatrixInfo import blosum50
from Bio.SubsMat.MatrixInfo import blosum45
from Bio.SubsMat.MatrixInfo import blosum40
from Bio.SubsMat.MatrixInfo import blosum35
from Bio.SubsMat.MatrixInfo import blosum30
from tkinter import filedialog
from tkinter import *
import tkinter as tk
def blosumalign(matrix , type , gapopen , gapextend ):
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    sv3 = StringVar()
    Label(win, text="First Sequence" , font=('Ubuntu Medium', 10, 'bold'), fg='black',bd=10).grid(row=0)
    Label(win, text="Second Sequence", font=('Ubuntu Medium', 10, 'bold'), fg='black',bd=10).grid(row=1)
    Label(win, text="Output Result", font=('Ubuntu Medium', 10, 'bold'), fg='black',bd=10).grid(row=2)

    e1 = Entry(win, textvariable=sv1)
    e2 = Entry(win, textvariable=sv2)
    e3 = Entry(win, textvariable=sv3)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    def inpo1():
        namein = filedialog.askopenfilename(parent=win)
        e1.insert(END, namein)
        print(e1.get())

    def inpo2():
        namein = filedialog.askopenfilename(parent=win)
        e2.insert(END, namein)
        print(e2.get())


    def inpo3():
        namein = filedialog.asksaveasfilename(parent=win)
        e3.insert(END, namein)
        print(e3.get())

    def out():
        infile1 = e1.get()
        infile2 = e2.get()
        outfile = e3.get()

        for record in SeqIO.parse(infile1, "fasta"):
            seq1 = record.seq
            seq1name = record.id

        for record in SeqIO.parse(infile2, "fasta"):
            seq2 = record.seq
            seq2name = record.id

        file = open(outfile, "w")
        #file.write("blablablabla")
        blomat = matrix
        log = type
        metadata = "#########################################\n# First Sequence Length: %s\n" \
                   "# First Sequence Name: %s\n# First Secuence File :%s\n" \
                   "# Second Sequence Length: %s\n# Second Sequence Name: %s\n" \
                   "# Second Sequence File: %s\n# Output Result File: %s\n# Program: Pairwise\n# Matrix: %s\n" \
                   "# Type: %s\n# Gap Open: %s\n# Gap Extend: %s\n# Note: Given Result May Contain Different Alignment with" \
                   "Different Scores or Different Alignment With The Same Score.\n#########################################\n\n" \
                   "" % (len(seq1),seq1name, infile1, len(seq2),seq2name,infile2,outfile, blomat, log ,gapopen,gapextend)
        file.write(metadata)
        print(blomat)
        print(log)
        if blomat == "BLOSUM 30":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum30, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum30, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
        elif blomat == "BLOSUM 35":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum35, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum35, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
        elif blomat == "BLOSUM 40":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum40, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum40, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
        elif blomat == "BLOSUM 45":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum45, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum45, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
        elif blomat == "BLOSUM 50":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum50, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum50, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "BLOSUM 55":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum55, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum55, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "BLOSUM 60":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum60, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum60, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "BLOSUM 62":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum62, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum62, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "BLOSUM 65":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum65, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum65, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "BLOSUM 70":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum70, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum70, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "BLOSUM 75":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum75, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum75, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)


        elif blomat == "BLOSUM 80":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum80, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum80, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "BLOSUM 85":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum85, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum85, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "BLOSUM 90":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum90, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum90, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "BLOSUM 95":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum95, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum95, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "BLOSUM 100":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, blosum100, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, blosum100, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
        file.close()

        win.destroy()

        r = open(outfile, 'r').read()
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
        T.insert(END, quote)
        mainloop()


    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo3).grid(row=2, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=3, column=1, sticky=W, pady=4, padx=40)

    win.mainloop()

#blosumalign("BLOSUM 30" , "Local" ,"-11" , "-1")









