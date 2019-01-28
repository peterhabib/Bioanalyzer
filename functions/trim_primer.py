from tkinter import filedialog
from tkinter import *
import tkinter as tk
from Bio import SeqIO
def tprimer():
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    sv3 = StringVar()
    Label(win, text="FASTAQ Record:").grid(row=0)
    Label(win, text="Primer List:").grid(row=1)
    Label(win, text="Output File:").grid(row=2)

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
        namein = filedialog.asksaveasfilename(parent=win)
        e2.insert(END, namein)
        print(e2.get())

    def out():
        records = e1,get()
        filepath = e2.get()
        outfile = e3.get()
        print("LOADING.....")

        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                # print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                # print(line)
                cnt += 1

        with open(outfile, "w") as f:
            trimmed_primer_reads = (rec[11:] for rec in \
                                    SeqIO.parse(records, "fastq") \
                                    if rec.seq.startswith(line))
            count = SeqIO.write(trimmed_primer_reads, f, "fastq")

        print("Finished!")



        win.destroy()



    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()




