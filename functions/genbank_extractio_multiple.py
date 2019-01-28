from Bio import SeqIO
import os.path
from tkinter import filedialog
from tkinter import *
import tkinter as tk
def multigbk(get1,get2,get3,get4,get5,get6,getradio):
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    Label(win, text="Input GenBank File").grid(row=0)


    e1 = Entry(win, textvariable=sv1)


    e1.grid(row=0, column=1)


    def inpo1():
        namein = filedialog.askopenfilename(parent=win)
        e1.insert(END, namein)
        print(e1.get())

    def out():
        infile = e1.get()
        tell1 = get1
        tell2 = get2
        tell3 = get3
        tell4 = get4
        tell5 = get5
        tell6 = get6
        Radio = getradio
        try:

            filename = infile
            gb = ".gbk"
            gbk = ".gb"

            if gb in filename:
                print(filename)
                dir = filename.replace(".gbk", " ")
                print(dir)
            else:
                dir = filename.replace("gb", " ")
            newpath = dir
            print(newpath)
            if not os.path.exists(str(newpath)):
                os.makedirs(newpath)

        except FileNotFoundError:
            return

            # loop to read records in file
        record = SeqIO.read(filename, "genbank")
        for feature in record.features:
            save_path = dir
            if Radio == '1':
                seq = "%s" % feature.qualifiers.get("gene")
            if Radio == '2':
                seq = "%s" % feature.qualifiers.get("product")
            if Radio == '3':
                seq = "%s" % feature.qualifiers.get("protein_id")
            if Radio == '4':
                seq = "%s" % feature.qualifiers.get("codon_start")
            if Radio == '5':
                seq = "%s" % feature.qualifiers.get("translation")
            if Radio == '6':
                seq = "%s" % feature.qualifiers.get("transl_table")

            a = seq.replace("[", "")
            b = a.replace("]", "")
            d = b.strip('\'')
            name_of_file = d
            completeName = os.path.join(save_path, str(name_of_file) + ".txt")
            file1 = open(completeName, "w")
            if tell1 == True and tell2 == False and tell3 == False and tell4 == False and tell5 == False and tell6 == False:
                gene = "Gene: %s" % feature.qualifiers.get("gene")
                File_content = "Gene: %s" % gene
                file1.write(File_content)
            if tell1 == False and tell2 == True and tell3 == False and tell4 == False and tell5 == False and tell6 == False:
                product = "Product: %s" % feature.qualifiers.get("product")
                File_content = "Product: %s" % product
                file1.write(File_content)
            if tell1 == False and tell2 == False and tell3 == True and tell4 == False and tell5 == False and tell6 == False:
                proteinid = "%s" % feature.qualifiers.get("protein_id")
                File_content = "Protein ID: %s" % proteinid
                file1.write(File_content)
            if tell1 == False and tell2 == False and tell3 == False and tell4 == True and tell5 == False and tell6 == False:
                File_content = "Codon Start: %s" % feature.qualifiers.get("codon_start")
                file1.write(File_content)
            if tell1 == False and tell2 == False and tell3 == False and tell4 == False and tell5 == True and tell6 == False:
                File_content = "Translation: %s" % feature.qualifiers.get("translation")
                file1.write(File_content)
            if tell1 == False and tell2 == False and tell3 == False and tell4 == False and tell5 == False and tell6 == True:
                File_content = "Translation Table: %s" % feature.qualifiers.get("transl_table")
                file1.write(File_content)

            # tell1
            if tell1 == True and tell2 == True and tell3 == False and tell4 == False and tell5 == False and tell6 == False:
                File_content = "Gene: %s\nproduct: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"))
                file1.write(File_content)

            if tell1 == True and tell2 == False and tell3 == True and tell4 == False and tell5 == False and tell6 == False:
                File_content = "Gene: %s\nProtein id: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("protein_id"))
                file1.write(File_content)

            if tell1 == True and tell2 == False and tell3 == False and tell4 == True and tell5 == False and tell6 == False:
                File_content = "Gene: %s\nCodon Start: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("codon_start"))
                file1.write(File_content)

            if tell1 == True and tell2 == False and tell3 == False and tell4 == False and tell5 == True and tell6 == False:
                File_content = "Gene: %s\nTranslation: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == True and tell2 == False and tell3 == False and tell4 == False and tell5 == False and tell6 == True:
                File_content = "Gene: %s\nTranslation Tables: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell2

            if tell1 == False and tell2 == True and tell3 == True and tell4 == False and tell5 == False and tell6 == False:
                File_content = "tell2product: %s\nProtein id: %s" % (
                    feature.qualifiers.get("product"), feature.qualifiers.get("protein_id"))
                file1.write(File_content)

            if tell1 == False and tell2 == True and tell3 == False and tell4 == True and tell5 == False and tell6 == False:
                File_content = "product: %s\nCodon Start: %s" % (
                    feature.qualifiers.get("product"), feature.qualifiers.get("codon_start"))
                file1.write(File_content)

            if tell1 == False and tell2 == True and tell3 == False and tell4 == False and tell5 == True and tell6 == False:
                File_content = "product: %s\nTranslation: %s" % (
                    feature.qualifiers.get("product"), feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == False and tell2 == True and tell3 == False and tell4 == False and tell5 == False and tell6 == True:
                File_content = "product: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("product"), feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell3

            if tell1 == False and tell2 == False and tell3 == True and tell4 == True and tell5 == False and tell6 == False:
                File_content = "Protein id: %s\nCodon Start: %s" % (
                    feature.qualifiers.get("protein_id"), feature.qualifiers.get("codon_start"))
                file1.write(File_content)

            if tell1 == False and tell2 == False and tell3 == True and tell4 == False and tell5 == True and tell6 == False:
                File_content = "Protein id: %s\nTranslation: %s" % (
                    feature.qualifiers.get("protein_id"), feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == False and tell2 == False and tell3 == True and tell4 == False and tell5 == False and tell6 == True:
                File_content = "Protein id: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("protein_id"), feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell4

            if tell1 == False and tell2 == False and tell3 == False and tell4 == True and tell5 == True and tell6 == False:
                File_content = "Codon Start: %s\nTranslation: %s" % (
                    feature.qualifiers.get("codon_start"), feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == False and tell2 == False and tell3 == False and tell4 == True and tell5 == False and tell6 == True:
                File_content = "Codon Start: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("codon_start"), feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell5

            if tell1 == False and tell2 == False and tell3 == False and tell4 == False and tell5 == True and tell6 == True:
                File_content = "Translation: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("translation"), feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell1,2

            if tell1 == True and tell2 == True and tell3 == True and tell4 == False and tell5 == False and tell6 == False:
                File_content = "Gene: %s\nproduct: %s\nProtein id: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("protein_id"))
                file1.write(File_content)

            if tell1 == True and tell2 == True and tell3 == False and tell4 == True and tell5 == False and tell6 == False:
                File_content = "Gene: %s\nproduct: %s\nCodon Start: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("codon_start"))
                file1.write(File_content)

            if tell1 == True and tell2 == True and tell3 == False and tell4 == False and tell5 == True and tell6 == False:
                File_content = "Gene: %s\nproduct: %s\nTranslation: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == True and tell2 == True and tell3 == False and tell4 == False and tell5 == False and tell6 == True:
                File_content = "Gene: %s\nproduct: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell 1,3

            if tell1 == True and tell2 == False and tell3 == True and tell4 == True and tell5 == False and tell6 == False:
                File_content = "Gene: %s\nProtein id: %s\nCodon Start: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"))
                file1.write(File_content)

            if tell1 == True and tell2 == False and tell3 == True and tell4 == False and tell5 == True and tell6 == False:
                File_content = "Gene: %s\nProtein id: %s\nTranslation: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == True and tell2 == False and tell3 == True and tell4 == False and tell5 == False and tell6 == True:
                File_content = "Gene: %s\nProtein id: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell 1,4

            if tell1 == True and tell2 == False and tell3 == False and tell4 == True and tell5 == True and tell6 == False:
                File_content = "Gene: %s\nCodon Start: %s\nTranslation: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("codon_start"),
                    feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == True and tell2 == False and tell3 == False and tell4 == True and tell5 == False and tell6 == True:
                File_content = "Gene: %s\nCodon Start: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("codon_start"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell 1,5

            if tell1 == True and tell2 == False and tell3 == False and tell4 == False and tell5 == True and tell6 == True:
                File_content = "Gene: %s\nTranslation: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("translation"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell1,2,3
            if tell1 == True and tell2 == True and tell3 == True and tell4 == True and tell5 == False and tell6 == False:
                File_content = "Gene: %s\nproduct: %s\nProtein id: %s\nCodon Start: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"))
                file1.write(File_content)

            if tell1 == True and tell2 == True and tell3 == True and tell4 == False and tell5 == True and tell6 == False:
                File_content = "Gene: %s\nproduct: %s\nProtein id: %s\nTranslation: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == True and tell2 == True and tell3 == True and tell4 == False and tell5 == False and tell6 == True:
                File_content = "Gene: %s\nproduct: %s\nProtein id: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell1,2,4

            if tell1 == True and tell2 == True and tell3 == False and tell4 == True and tell5 == True and tell6 == False:
                File_content = "Gene: %s\nproduct: %s\nCodon Start: %s\nTranslation: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("codon_start"),
                    feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == True and tell2 == True and tell3 == False and tell4 == True and tell5 == False and tell6 == True:
                File_content = "Gene: %s\nproduct: %s\nCodon Start: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("codon_start"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell1,2,5

            if tell1 == True and tell2 == True and tell3 == False and tell4 == False and tell5 == True and tell6 == True:
                File_content = "Gene: %s\nproduct: %s\nTranslation: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("translation"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell1,2,3,4

            if tell1 == True and tell2 == True and tell3 == True and tell4 == True and tell5 == True and tell6 == False:
                File_content = "Gene: %s\nproduct: %s\nProtein id: %s\nCodon Start: %s\nTranslation: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"), feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == True and tell2 == True and tell3 == True and tell4 == True and tell5 == False and tell6 == True:
                File_content = "Gene: %s\nproduct: %s\nProtein id: %s\nCodon Start: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"), feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell1,2,3,4,5

            if tell1 == True and tell2 == True and tell3 == True and tell4 == True and tell5 == True and tell6 == True:
                gene = feature.qualifiers.get("gene")
                product = feature.qualifiers.get("product")
                proteinid = feature.qualifiers.get("protein_id")
                codon = feature.qualifiers.get("codon_start")
                translation = feature.qualifiers.get("translation")
                transtable = feature.qualifiers.get("transl_table")
                File_content1 = "Gene: %s\nproduct: %s\nProtein id: %s" % (gene, product, proteinid)
                File_content2 = "Codon Start: %s\nTranslation: %s\nTranslation Table: %s" % (
                    codon, translation, transtable)
                file1.write(File_content1)
                file1.write(File_content2)

            # tell1,3,4
            if tell1 == True and tell2 == False and tell3 == True and tell4 == True and tell5 == True and tell6 == False:
                File_content = "Gene: %s\nproduct: %s\nProtein id: %s\nCodon Start: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"))
                file1.write(File_content)

            if tell1 == True and tell2 == False and tell3 == True and tell4 == True and tell5 == False and tell6 == True:
                File_content = "Gene: %s\nproduct: %s\nProtein id: %s\nTranslation: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("translation"))
                file1.write(File_content)

            # tell1,3,5

            if tell1 == True and tell2 == False and tell3 == True and tell4 == False and tell5 == True and tell6 == True:
                File_content = "Gene: %s\nproduct: %s\nTranslation: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("translation"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell1,3,4,5

            if tell1 == True and tell2 == False and tell3 == True and tell4 == True and tell5 == True and tell6 == True:
                File_content = "Gene: %s\nproduct: %s\nProtein id: %s\nCodon Start: %s\nTranslation: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"), feature.qualifiers.get("translation"))
                file1.write(File_content)

            # tell1,4,5
            if tell1 == True and tell2 == False and tell3 == False and tell4 == True and tell5 == True and tell6 == True:
                File_content = "Gene: %s\nproduct: %s\nProtein id: %s\nCodon Start: %s\nTranslation: %s" % (
                    feature.qualifiers.get("gene"), feature.qualifiers.get("product"),
                    feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"), feature.qualifiers.get("translation"))
                file1.write(File_content)

            # tell2,3

            if tell1 == False and tell2 == True and tell3 == True and tell4 == True and tell5 == False and tell6 == False:
                File_content1 = "product: %s\nProtein id: %s\nCodon Start: %s" % (
                    feature.qualifiers.get("product"), feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"))
                file1.write(File_content1)

            if tell1 == False and tell2 == True and tell3 == True and tell4 == False and tell5 == True and tell6 == False:
                File_content1 = "product: %s\nProtein id: %s\nTranslation: %s" % (
                    feature.qualifiers.get("product"), feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("translation"))
                file1.write(File_content1)

            if tell1 == False and tell2 == True and tell3 == True and tell4 == False and tell5 == False and tell6 == True:
                File_content1 = "product: %s\nProtein id: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("product"), feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content1)

            # tell2,3,4

            if tell1 == False and tell2 == True and tell3 == True and tell4 == True and tell5 == True and tell6 == False:
                print("xxxxxxxxx")
                File_content1 = "product: %s\nProtein id: %s\nCodon Start: %s\nTranslation: %s" % (
                    feature.qualifiers.get("product"), feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"), feature.qualifiers.get("translation"))
                file1.write(File_content1)

            if tell1 == False and tell2 == True and tell3 == True and tell4 == True and tell5 == False and tell6 == True:
                File_contentz = "product: %s\nProtein id: %s\nCodon Start: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("product"), feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"), feature.qualifiers.get("transl_table"))
                file1.write(File_contentz)

            # tell2,3,4,5

            if tell1 == False and tell2 == True and tell3 == True and tell4 == True and tell5 == True and tell6 == True:
                File_content = "product: %s\nProtein id: %s\nCodon Start: %s\nTranslation: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("product"), feature.qualifiers.get("protein_id"),
                    feature.qualifiers.get("codon_start"), feature.qualifiers.get("translation"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell3,4

            if tell1 == False and tell2 == False and tell3 == True and tell4 == True and tell5 == True and tell6 == False:
                File_content = "Protein id: %s\nCodon Start: %s\nTranslation: %s" % (
                    feature.qualifiers.get("protein_id"), feature.qualifiers.get("codon_start"),
                    feature.qualifiers.get("translation"))
                file1.write(File_content)

            if tell1 == False and tell2 == False and tell3 == True and tell4 == True and tell5 == False and tell6 == True:
                File_content = "Protein id: %s\nCodon Start: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("protein_id"), feature.qualifiers.get("codon_start"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell 3,4,5

            if tell1 == False and tell2 == False and tell3 == True and tell4 == True and tell5 == True and tell6 == True:
                File_content = "Protein id: %s\nCodon Start: %s\nTranslation: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("protein_id"), feature.qualifiers.get("codon_start"),
                    feature.qualifiers.get("translation"), feature.qualifiers.get("transl_table"))
                file1.write(File_content)

            # tell 4,5
            if tell1 == False and tell2 == False and tell3 == False and tell4 == True and tell5 == True and tell6 == True:
                File_content = "Codon Start: %s\nTranslation: %s\nTranslation Table: %s" % (
                    feature.qualifiers.get("codon_start"), feature.qualifiers.get("translation"),
                    feature.qualifiers.get("transl_table"))
                file1.write(File_content)

        win.destroy()

    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=3, column=1, sticky=W, pady=4, padx=40)

    mainloop()



#multigbk('1','1','1','1','1','1','1')