from Bio.pairwise2 import format_alignment
from Bio import SeqIO
from Bio import pairwise2
from tkinter import filedialog
from tkinter import *
import tkinter as tk

def glomsalign(gopen , gexten):

    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    sv3 = StringVar()
    Label(win, text="First FASTA Record").grid(row=0)
    Label(win, text="Second FASTA Record").grid(row=1)
    Label(win, text="Output Result File").grid(row=2)

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
        infile1 = "%s"%e1.get()
        infile2 = "%s"%e2.get()
        outfile = "%s"%e3.get()
        for seq_record1 in SeqIO.parse(infile1, "fasta"):
            seq1 = seq_record1.seq
            seq1name = seq_record1.id
            lens1 = len(seq1)
            print(len(seq1))
            print(" ")
        for seq_record2 in SeqIO.parse(str(infile2), "fasta"):
            seq2 = seq_record2.seq
            seq2name = seq_record2.id
            lens2 = len(seq2)
            print(lens2)
            val = lens2//2

        file = open(outfile, "w")
        metadata = "#########################################\n# First Sequence Length: %s\n" \
                   "# First Sequence Name: %s\n# First Secuence File :%s\n" \
                   "# Second Sequence Length: %s\n# Second Sequence Name: %s\n" \
                   "# Second Sequence File: %s\n# Output Result File: %s\n# Program: Pairwise\n" \
                   "# Type: Global\n# Gap Open: %s\n# Gap Extend: %s\n# Note: Given Result May Contain Different Alignment with" \
                   "Different Scores or Different Alignment With The Same Score.\n#########################################\n\n" \
                   "" % (
                   len(seq1), seq1name, infile1, len(seq2), seq2name, infile2, outfile, gopen, gexten)
        file.write(metadata)


        for a in pairwise2.align.globalms(seq1, seq2,1 ,-1, int(gopen), int(gexten)):
            print(format_alignment(*a))
            alignments2 = format_alignment(*a)
            file.write("%s\n\n" % alignments2)

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
        T.tag_configure('color', foreground='black', font=('Arial', 10, 'bold'))
        quote = r
        T.insert(END, quote, 'color')
        mainloop()



    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo3).grid(row=2, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=3, column=1, sticky=W, pady=4, padx=40)

    mainloop()


#glomsalign("-11","-1")