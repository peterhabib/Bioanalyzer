from Bio.Emboss.Applications import WaterCommandline
from Bio import AlignIO
from tkinter import *
from tkinter import filedialog
from tkinter import *
import tkinter as tk


def nmwwater(gapopen , gapextend):
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    sv3 = StringVar()
    Label(win, text="First FASTA Record").grid(row=0)
    Label(win, text="First FASTA Record").grid(row=1)
    Label(win, text="Output File").grid(row=2)

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
        filename1 = e1.get()
        filename2 = e2.get()
        outfile = e3.get()

        needle_cline = WaterCommandline()
        needle_cline.asequence = filename1
        needle_cline.bsequence = filename2
        needle_cline.gapopen = int(gapopen)
        needle_cline.gapextend = int(gapextend)
        needle_cline.outfile = "needle.txt"
        print(needle_cline)
        print(needle_cline.outfile)
        stdout, stderr = needle_cline()
        print(stdout + stderr)
        align = AlignIO.read("needle.txt", "emboss")
        file = open("needle.txt", "r")
        # print(file.read())
        view = ("\n\n%s" % file.read())
        root = Tk()
        S = Scrollbar(root)
        T = Text(root, height=4, width=500)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        T.insert(END, view)

        with open(outfile, "w") as f:
            f.write(view)



    Button(win, text='choose..', command=inpo1).grid(row=0, column=3, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=3, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo3).grid(row=2, column=3, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=4, column=1, sticky=W, pady=4, padx=40)

    mainloop()


#nmwwater("-11" , "-1")