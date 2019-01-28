from Bio import Entrez
from Bio import Medline
from tkinter import *
from tkinter import filedialog
import tkinter as tk

def pubm(query):
    handle = Entrez.esearch(db="pubmed", term="%s" % query, retmax=1000000000)
    Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
    record = Entrez.read(handle)
    idlist = record["IdList"]
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    records = list(records)
    file = open("result.txt", "w")
    for record in records:
        print("title:", record.get("TI", "?"))
        print("authors:", record.get("AU", "?"))
        print("source:", record.get("SO", "?"))
        print("")
        tit = "title:%s" % record.get("TI", "?")
        d = "ID:", record.get("PMID", "?")
        content = "%s\n%s\n\n" % (tit, d)
        file.write(content)
    file.close()


    root = Tk()
    S = Scrollbar(root)
    fileview = open("result.txt" , "r")
    T = Text(root, height=50, width=500)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    S.config(command=T.xview)
    T.config(yscrollcommand=S.set)
    T.config(xscrollcommand=S.set)
    quote = fileview.read()
    T.insert(END, quote, 'color')
    mainloop()




