from Bio.Blast import NCBIWWW , NCBIXML
from tkinter import filedialog
from tkinter import *
import tkinter as tk
def openblasts(program , database , align):
    chos = program
    db = database
    aligns = align
    print(aligns)
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    Label(win, text="Input ID").grid(row=0)
    Label(win, text="Output Result").grid(row=1)

    e1 = Entry(win, textvariable=sv1)
    e2 = Entry(win, textvariable=sv2)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)


    def inpo2():
        namein = filedialog.asksaveasfilename(parent=win)
        e2.insert(END, namein)
        print(e2.get())

    def out():
        inid = e1.get()
        outfile = e2.get()
        if aligns == "1":
            if chos == 'BLASTn':
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "nt", "%d"% inid)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_rna", "%s" % inid)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbnt", "%s" % inid)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "nr", "%s" % inid)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_protein", "%s" % inid)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "swissprot", "%s" % inid)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "est", "%s" % inid)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "est", "%s" % inid)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_representative_genomes", "%s" % inid)




                blast_record = NCBIXML.read(result_handle)
                file = open("lines.txt", "w")
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        if 1 == 1:
                            print("****Alignment****")
                            print("sequence:", alignment.title)
                            print("length:", alignment.length)
                            print("e value:", hsp.expect)
                            print(hsp.query[0:75] + "...")
                            print(hsp.sbjct[0:75] + "...")
                            view = "sequence:%s\nlength:%s\ne value:%s\n%s\n%s\n%s\n\n" % (
                                alignment.title, alignment.length, hsp.expect, hsp.query[0:100] + "...",
                                hsp.match[0:100] + "...", hsp.sbjct[0:100] + "...")
                            file.write(view)
                file = open(outfile, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

            elif chos == 'BLASTp':
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "nt", "%s" % inid)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_rna", "%s" % inid)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbnt", "%s" % inid)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "nr", "%s" % inid)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_protein", "%s" % inid)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "swissprot", "%s" % inid)
                elif db == 'PDB protein database(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbaa", "%s" % inid)
                blast_record = NCBIXML.read(result_handle)
                file = open("lines.txt", "w")
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        if 1 == 1:
                            print("****Alignment****")
                            print("sequence:", alignment.title)
                            print("length:", alignment.length)
                            print("e value:", hsp.expect)
                            print(hsp.query[0:75] + "...")
                            print(hsp.sbjct[0:75] + "...")
                            view = "sequence:%s\nlength:%s\ne value:%s\n%s\n%s\n%s\n\n" % (
                                alignment.title, alignment.length, hsp.expect, hsp.query[0:100] + "...",
                                hsp.match[0:100] + "...", hsp.sbjct[0:100] + "...")
                            file.write(view)
                file = open(outfile, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

            elif chos == 'tBLASTn':

                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "nt", "%s" % inid)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_rna", "%s" % inid)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbnt", "%s" % inid)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "nr", "%s" % inid)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_protein", "%s" % inid)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "swissprot", "%s" % inid)
                elif db == 'PDB protein database(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbaa", "%s" % inid)
                blast_record = NCBIXML.read(result_handle)
                file = open("lines.txt", "w")
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        if 1 == 1:
                            print("****Alignment****")
                            print("sequence:", alignment.title)
                            print("length:", alignment.length)
                            print("e value:", hsp.expect)
                            print(hsp.query[0:75] + "...")
                            print(hsp.sbjct[0:75] + "...")
                            view = "sequence:%s\nlength:%s\ne value:%s\n%s\n%s\n%s\n\n" % (
                                alignment.title, alignment.length, hsp.expect, hsp.query[0:100] + "...",
                                hsp.match[0:100] + "...", hsp.sbjct[0:100] + "...")

                            file.write(view)

                file = open(outfile, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

            elif chos == 'BLASTx':

                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "nt", "%s" % inid)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_rna", "%s" % inid)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbnt", "%s" % inid)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "nr", "%s" % inid)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_protein", "%s" % inid)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "swissprot", "%s" % inid)
                elif db == 'PDB protein database(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbaa", "%s" % inid)
                blast_record = NCBIXML.read(result_handle)

                file = open("lines.txt", "w")
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        if 1 == 1:
                            print("****Alignment****")
                            print("sequence:", alignment.title)
                            print("length:", alignment.length)
                            print("e value:", hsp.expect)
                            print(hsp.query[0:75] + "...")
                            print(hsp.sbjct[0:75] + "...")
                            view = "sequence:%s\nlength:%s\ne value:%s\n%s\n%s\n%s\n\n" % (
                                alignment.title, alignment.length, hsp.expect, hsp.query[0:100] + "...",
                                hsp.match[0:100] + "...", hsp.sbjct[0:100] + "...")

                            file.write(view)

                file = open(outfile, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

            elif chos == 'tBLASTx':

                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "nt", "%s" % inid)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_rna", "%s" % inid)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbnt", "%s" % inid)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "nr", "%s" % inid)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_protein", "%s" % inid)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "swissprot", "%s" % inid)
                elif db == 'PDB protein database(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbaa", "%s" % inid)
                with open("Blast Result.xml", "w") as out_handle:
                    out_handle.write(result_handle.read())
                result_handle.close()
                blast_qresult = SearchIO.read('Blast Result.xml', 'blast-xml')
                print(blast_qresult)


                blast_record = NCBIXML.read(result_handle)

                file = open("lines.txt", "w")
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        if 1 == 1:
                            print("****Alignment****")
                            print("sequence:", alignment.title)
                            print("length:", alignment.length)
                            print("e value:", hsp.expect)
                            print(hsp.query[0:75] + "...")
                            print(hsp.sbjct[0:75] + "...")
                            view = "sequence:%s\nlength:%s\ne value:%s\n%s\n%s\n%s\n\n" % (
                                alignment.title, alignment.length, hsp.expect, hsp.query[0:100] + "...",
                                hsp.match[0:100] + "...", hsp.sbjct[0:100] + "...")

                            file.write(view)

                file = open(outfile, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

        win.destroy()


    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()


