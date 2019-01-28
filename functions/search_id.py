from tkinter import filedialog
from tkinter import *
import tkinter as tk
from Bio import Entrez
from Bio import SeqIO
def search(datab,outtype,idnum):

    #Entrez.email = "%s" % e2.get()
    handle = Entrez.efetch(db=datab, rettype=outtype, retmode="text", id=idnum)
    record = handle.read()
    print(record)

    root = Tk()
    S = Scrollbar(root)
    T = Text(root, height=50, width=500)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    S.config(command=T.xview)
    T.config(yscrollcommand=S.set)
    T.config(xscrollcommand=S.set)
    quote = record
    T.insert(END, quote, 'color')
    mainloop()

