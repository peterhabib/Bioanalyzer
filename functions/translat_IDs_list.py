from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk

def translids(table2 , tostop2):
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    Label(win, text="ID List").grid(row=0)
    Label(win, text="Output Result File").grid(row=1)

    e1 = Entry(win, textvariable=sv1)
    e2 = Entry(win, textvariable=sv2)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    def inpo1():
        namein = filedialog.askopenfilename(parent=win)
        e1.insert(END, namein)
        print(e1.get())

    def inpo2():
        namein = filedialog.asksaveasfilename(parent=win)
        e2.insert(END, namein)
        print(e2.get())

    def out():
        infile = e1.get()
        outfile = e2.get()

        try:
            ides = open(infile).readlines()
            codont2 = table2
            tos2 = tostop2
        except FileNotFoundError:
            return

        fasta = open("result.fasta", "w")
        f = open(outfile, "w")
        if True:
            for line in ides:
                ln = line
                Entrez.email = "your.email@helsinki.fi"
                handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id=ln)
                record = handle.read()
                print(record)
                fasta.write(str(record))

            for record in SeqIO.parse("result.fasta", "fasta"):
                if codont2 == "Standard":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=1, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=1, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))

                elif codont2 == "Vertebrate Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=2, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=2, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))

                elif codont2 == "Yeast Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=3, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=3, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))

                elif codont2 == "Mold Mitochondrial; Protozoan Mitochondrial; Coelenterate Mitochondrial; Mycoplasma; Spiroplasma":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=4, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=4, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))



                elif codont2 == "Invertebrate Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=5, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=5, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))


                elif codont2 == "Ciliate Nuclear; Dasycladacean Nuclear; Hexamita Nuclear":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=6, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=6, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))



                elif codont2 == "Echinoderm Mitochondrial; Flatworm Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=9, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=9, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))



                elif codont2 == "Euplotid Nuclear":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=10, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=10, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))



                elif codont2 == "Bacterial, Archaeal and Plant Plastid":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=11, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=11, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))



                elif codont2 == "Alternative Yeast Nuclear":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=12, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=12, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))



                elif codont2 == "Ascidian Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=13, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=13, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))




                elif codont2 == "Alternative Flatworm Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=14, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=14, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))



                elif codont2 == "Blepharisma Macronuclear":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=15, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=15, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))



                elif codont2 == "Chlorophycean Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=16, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=16, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))




                elif codont2 == "Trematode Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=21, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=21, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))





                elif codont2 == "Scenedesmus obliquus Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=22, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=22, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))





                elif codont2 == "Thraustochytrium Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=23, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=23, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))


                elif codont2 == "Pterobranchia Mitochondrial":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=24, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=24, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))

                elif codont2 == "Candidate Division SR1 and Gracilibacteria":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=25, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=25, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))


                elif codont2 == "Pachysolen tannophilus Nuclear":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=26, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=26, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))


                elif codont2 == "Karyorelict Nuclear":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=27, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=27, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))


                elif codont2 == "Condylostoma Nuclear":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=28, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=28, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))


                elif codont2 == "Mesodinium Nuclear":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=29, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=29, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))



                elif codont2 == "Peritrich Nuclear":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=30, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=30, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))



                elif codont2 == "Blastocrithidia Nuclear":
                    if tos2 == 1:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=31, to_stop=True)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))
                    else:
                        print(">%s" % record.id)
                        coding_dna = Seq("%s" % record.seq)
                        translate = coding_dna.translate(table=31, to_stop=False)
                        print("%s" % translate)
                        f.write(str(">%s\n%s\n\n" % (record.id, translate)))

            # if os.path.exists("result.fasta"):
            #     os.remove("result.fasta")

        f.close()
        fasta.close()

        r = open(e2.get(), 'r').read()
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
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()

# translids("Blastocrithidia Nuclear" , "0")

