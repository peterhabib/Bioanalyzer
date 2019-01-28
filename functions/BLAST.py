from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW
import tkinter
from Bio import SeqIO
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
#infile , outfile , program , database , align

def blast(program , database , alignz):
    chos = program
    db = database
    aligns = alignz
    print(aligns)
    win = tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    Label(win, text="Input FASTA Sequence").grid(row=0)
    Label(win, text="Save Output Result").grid(row=1)

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
        file = open("lines.txt" , "w")

        if aligns == "0":
            if chos == 'BLASTn':

                record = SeqIO.read(str(e1.get()), "fasta")
                ser = record.seq
                print(ser)
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "nt", ser)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_rna", ser)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbnt", ser)
                elif db == 'Non-redundant(Protein)':
                    err()
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    err()
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    err()
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "est", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "est", ser)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_representative_genomes", ser)

                blast_record = NCBIXML.read(result_handle)
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
                            T.insert(END, view)
                            file.write(view)

                filename = e2.get()
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file = open(filename, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

            elif chos == 'BLASTp':

                record = SeqIO.read(str(e1.get()), "fasta")
                ser = record.seq
                print(ser)
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "nt", ser)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "refseq_rna", ser)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "pdbnt", ser)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("blastp", "nr", ser)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("blastp", "refseq_protein", ser)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("blastp", "swissprot", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "est", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "est", ser)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "refseq_representative_genomes", ser)
                blast_record = NCBIXML.read(result_handle)

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
                                hsp.match[0:len(hsp.query)] + "...", hsp.sbjct[0:100] + "...")
                            T.insert(END, view)
                            file.write(view)

                filename = e2.get()
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file = open(filename, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

            elif chos == 'tBLASTn':

                record = SeqIO.read(str(e1.get()), "fasta")
                ser = record.seq
                print(ser)
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "nt", ser)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "refseq_rna", ser)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "pdbnt", ser)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("tblastn", "nr", ser)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("tblastn", "refseq_protein", ser)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("tblastn", "swissprot", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "est", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "est", ser)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "refseq_representative_genomes", ser)
                with open("Blast Result.xml", "w") as out_handle:
                    out_handle.write(result_handle.read())
                result_handle.close()
                blast_qresult = SearchIO.read('Blast Result.xml', 'blast-xml')

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
                                hsp.match[0:len(hsp.query)] + "...", hsp.sbjct[0:100] + "...")
                            T.insert(END, view)
                            file.write(view)

                filename = e2.get()
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file = open(filename, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

            elif chos == 'BLASTx':

                record = SeqIO.read(str(e1.get()), "fasta")
                ser = record.seq
                print(ser)
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "nt", ser)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "refseq_rna", ser)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "pdbnt", ser)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("blastx", "nr", ser)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("blastx", "refseq_protein", ser)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("blastx", "swissprot", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "est", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "est", ser)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "refseq_representative_genomes", ser)
                blast_record = NCBIXML.read(result_handle)

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
                                hsp.match[0:len(hsp.query)] + "...", hsp.sbjct[0:100] + "...")
                            T.insert(END, view)
                            file.write(view)

                filename = e2.get()
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file = open(filename, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

            elif chos == 'tBLASTx':

                record = SeqIO.read(str(e1.get()), "fasta")
                ser = record.seq
                print(ser)
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "nt", ser)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "refseq_rna", ser)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "pdbnt", ser)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("tblastx", "nr", ser)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("tblastx", "refseq_protein", ser)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("tblastx", "swissprot", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "est", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "est", ser)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "refseq_representative_genomes", ser)
                blast_record = NCBIXML.read(result_handle)

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
                            T.insert(END, view)
                            file.write(view)

                filename = e2.get()
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file = open(filename, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()


        elif aligns == "1":
            if chos == 'BLASTn':

                record = SeqIO.read(str(e1.get()), "fasta")
                ser = record.seq
                print(ser)
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "nt", ser)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_rna", ser)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "pdbnt", ser)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "nr", ser)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_protein", ser)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("blastn", "swissprot", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "est", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "est", ser)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("blastn", "refseq_representative_genomes", ser)

                blast_record = NCBIXML.read(result_handle)

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




                filename = e2.get()
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file = open(filename, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()




            elif chos == 'BLASTp':

                record = SeqIO.read(str(e1.get()), "fasta")
                ser = record.seq
                print(ser)
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "nt", ser)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "refseq_rna", ser)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "pdbnt", ser)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("blastp", "nr", ser)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("blastp", "refseq_protein", ser)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("blastp", "swissprot", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "est", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "est", ser)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("blastp", "refseq_representative_genomes", ser)

                blast_record = NCBIXML.read(result_handle)

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
                                alignment.title, alignment.length, hsp.expect, hsp.query[0:150] + "...",
                                hsp.match[0:100] + "...", hsp.sbjct[0:150] + "...")
                            T.insert(END, view)
                            file.write(view)

                filename = e2.get()
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file = open(filename, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()



            elif chos == 'tBLASTn':

                record = SeqIO.read(str(e1.get()), "fasta")
                ser = record.seq
                print(ser)
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "nt", ser)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "refseq_rna", ser)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "pdbnt", ser)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("tblastn", "nr", ser)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("tblastn", "refseq_protein", ser)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("tblastn", "swissprot", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "est", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "est", ser)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("tblastn", "refseq_representative_genomes", ser)
                blast_record = NCBIXML.read(result_handle)

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
                                alignment.title, alignment.length, hsp.expect, hsp.query[0:150] + "...",
                                hsp.match[0:150] + "...", hsp.sbjct[0:150] + "...")
                            T.insert(END, view)
                            file.write(view)

                filename = e2.get()
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file = open(filename, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

            elif chos == 'BLASTx':

                record = SeqIO.read(str(e1.get()), "fasta")
                ser = record.seq
                print(ser)
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "nt", ser)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "refseq_rna", ser)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "pdbnt", ser)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("blastx", "nr", ser)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("blastx", "refseq_protein", ser)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("blastx", "swissprot", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "est", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "est", ser)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("blastx", "refseq_representative_genomes", ser)
                blast_record = NCBIXML.read(result_handle)

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
                                alignment.title, alignment.length, hsp.expect, hsp.query[0:150] + "...",
                                hsp.match[0:100] + "...", hsp.sbjct[0:150] + "...")
                            T.insert(END, view)
                            file.write(view)

                filename = e2.get()
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file = open(filename, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

            elif chos == 'tBLASTx':
                record = SeqIO.read(str(e1.get()), "fasta")
                ser = record.seq
                print(ser)
                if db == 'Nucleotide collection(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "nt", ser)
                elif db == 'NCBI Transcript Ref_Seq(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "refseq_rna", ser)
                elif db == 'PDB nucleotide database(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "pdbnt", ser)
                elif db == 'Non-redundant(Protein)':
                    result_handle = NCBIWWW.qblast("tblastx", "nr", ser)
                elif db == 'NCBI Protein Ref_Seq(Protein)':
                    result_handle = NCBIWWW.qblast("tblastx", "refseq_protein", ser)
                elif db == 'Non-redundant UniProtKB/SwissProt(Protein)':
                    result_handle = NCBIWWW.qblast("tblastx", "swissprot", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "est", ser)
                elif db == 'Expressed Sequences tags(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "est", ser)
                elif db == 'RefSeq Representative Genome Database(DNA)':
                    result_handle = NCBIWWW.qblast("tblastx", "refseq_representative_genomes", ser)
                blast_record = NCBIXML.read(result_handle)

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
                                alignment.title, alignment.length, hsp.expect, hsp.query[0:150] + "...",
                                hsp.match[0:100] + "...", hsp.sbjct[0:150] + "...")
                            T.insert(END, view)
                            file.write(view)

                filename = e2.get()
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                file = open(filename, "w")
                reads = open("lines.txt")
                for i, line in enumerate(reads):
                    result = "%s" % line
                    file.write(result)
                reads.close()
                file.close()

        root = Tk()
        S = Scrollbar(root)
        dis = open("lines.txt", "r").read()
        T = Text(root, height=50, width=500)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        S.config(command=T.xview)
        T.config(yscrollcommand=S.set)
        T.config(xscrollcommand=S.set)
        T.insert(END, dis)
        mainloop()

    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()







