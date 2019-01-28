from Bio import SeqIO
from tkinter import filedialog
from tkinter import *
import tkinter as tk
def tadoptor():
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    sv3 = StringVar()
    Label(win, text="FastaQ Record:").grid(row=0)
    Label(win, text="Adapter List: ").grid(row=1)
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
        namein = filedialog.asksaveasfilename(parent=win)
        e2.insert(END, namein)
        print(e2.get())

    def out():
        inrecord = e1.get()
        inadaptors = e2.get()
        outfile = e3.get()

        def trim_adaptors(records, adaptor, min_len):
            len_adaptor = len(adaptor)  # cache this for later
            for record in records:
                len_record = len(record)  # cache this for later
                if len(record) < min_len:
                    continue
                index = record.seq.find(adaptor)
                if index == -1:
                    # adaptor not found, so won’t trim
                    yield record
                elif len_record - index - len_adaptor >= min_len:
                    # after trimming this will still be long enough
                    yield record[index + len_adaptor:]

        record = inrecord

        adaptor = inadaptors
        filepath = adaptor
        original_reads = SeqIO.parse(record, "fastq")

        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                # print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                # print(line)
                cnt += 1

        filename = outfile

        with open(filename, "w") as f:
            trimmed_reads = trim_adaptors(original_reads, line, 100)
            count = SeqIO.write(trimmed_reads, f, "fastq")
            f.write(str(count))

        win.destroy()

    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()






