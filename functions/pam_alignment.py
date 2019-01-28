from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat.MatrixInfo import pam30
from Bio.SubsMat.MatrixInfo import pam60
from Bio.SubsMat.MatrixInfo import pam90
from Bio.SubsMat.MatrixInfo import pam120
from Bio.SubsMat.MatrixInfo import pam180
from Bio.SubsMat.MatrixInfo import pam250
from Bio.SubsMat.MatrixInfo import pam300
from tkinter import filedialog
from tkinter import *
import tkinter as tk


def pamalign(matrix , type , gapopen , gapextend ):
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    sv3 = StringVar()
    Label(win, text="First FASTA Record:").grid(row=0)
    Label(win, text="Second FASTA Record:").grid(row=1)
    Label(win, text="Output Result File:").grid(row=2)

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

        fn1 = e1.get()
        for record in SeqIO.parse(fn1, "fasta"):
            seq1 = record.seq
            seq1name = record.id
            print(seq1)

        fn2 = e2.get()
        outfile = e3.get()
        for record in SeqIO.parse(fn2, "fasta"):
            seq2 = record.seq
            seq2name = record.id
            print(seq2)
        file = open(e3.get(), "w")
        blomat = matrix
        log = type


        metadata = "#########################################\n# First Sequence Length: %s\n" \
                   "# First Sequence Name: %s\n# First Secuence File :%s\n" \
                   "# Second Sequence Length: %s\n# Second Sequence Name: %s\n" \
                   "# Second Sequence File: %s\n# Output Result File: %s\n# Program: Pairwise\n# Matrix: %s\n" \
                   "# Type: %s\n# Gap Open: %s\n# Gap Extend: %s\n# Note: Given Result May Contain Different Alignment with" \
                   "Different Scores or Different Alignment With The Same Score.\n#########################################\n\n" \
                   "" % (
                   len(seq1), seq1name, fn1, len(seq2), seq2name, fn2, outfile, blomat, log, gapopen, gapextend)
        file.write(metadata)


        print(blomat)
        print(log)
        if blomat == "PAM 30":
            print("step1")
            if log == "Local":
                print("step2")
                for a in pairwise2.align.localds(seq1, seq2, pam30, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, pam30, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
        elif blomat == "PAM 60":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, pam60, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, pam60, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
        elif blomat == "PAM 90":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, pam90, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, pam90, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
        elif blomat == "PAM 120":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, pam120, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, pam120, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
        elif blomat == "PAM 180":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, pam180, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, pam180, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "PAM 250":
            if log == "Local":
                for a in pairwise2.align.localds(seq1, seq2, pam250, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globalds(seq1, seq2, pam250, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        elif blomat == "PAM 300":
            if log == "Local":
                for a in pairwise2.align.localdc(seq1, seq2, pam300, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)
            else:
                for a in pairwise2.align.globaldc(seq1, seq2, pam300, int(gapopen), int(gapextend)):
                    # print(format_alignment(*a))
                    alignments2 = pairwise2.format_alignment(*a)
                    print(alignments2)
                    file.write(alignments2)

        file.close()



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
        T.insert(END, quote, 'color')
        mainloop()




    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo3).grid(row=2, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=3, column=1, sticky=W, pady=4, padx=40)

    mainloop()


#pamalign("PAM 300" , "Local" , "-11" , "-1")