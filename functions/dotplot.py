from Bio import SeqIO
from tkinter import filedialog
from tkinter import *
import tkinter as tk
def dplot():
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    Label(win, text="First FASTA Record").grid(row=0)
    Label(win, text="Second FASTA record").grid(row=1)

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
        infile1 = e1.get()
        infile2 = e2.get()
        with open(infile1) as in_handle:
            record_iterator1 = SeqIO.parse(in_handle, "fasta")
            rec_one = next(record_iterator1)
        with open(infile2) as in_handle:
            record_iterator2 = SeqIO.parse(in_handle, "fasta")
            rec_two = next(record_iterator2)
        window = 7
        seq_one = str(rec_one.seq).upper()
        seq_two = str(rec_two.seq).upper()
        data = [[(seq_one[i:i + window] != seq_two[j:j + window])
                 for j in range(len(seq_one) - window)]
                for i in range(len(seq_two) - window)]
        import pylab
        pylab.gray()
        pylab.imshow(data)
        pylab.xlabel("%s (length %i bp)" % (rec_one.id, len(rec_one)))
        pylab.ylabel("%s (length %i bp)" % (rec_two.id, len(rec_two)))
        pylab.title("Dot plot using window size %i\n(allowing no mis-matches)" % window)
        pylab.show()


        win.destroy()



    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()
