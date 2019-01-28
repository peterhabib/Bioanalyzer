from Bio import Phylo
from Bio import SeqIO
import networkx, pylab
import pylab
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
import tkinter as tk
from tkinter import *
from tkinter import filedialog
def allphylo(choice):
    if choice == "1":

        win = tk.Tk()
        sv1 = StringVar()
        sv2 = StringVar()
        Label(win, text="Input File").grid(row=0)
        Label(win, text="Output File").grid(row=1)

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

            records = SeqIO.parse("%s"%e1.get(), "fasta")

            lens = []
            lens2 = []
            file = open("phylo.phy", 'w')
            for record in records:
                ids = record.id
                sequence = record.seq[0:100]
                lens.append(record.id)
                lens2.append(record.seq)
                line = "%s   %s" % (ids, sequence)
                print(line)

            lengthmax = len(max(lens, key=len))

            lengthmin = len(min(lens, key=len))

            file.write("   %s     100\n" % len(lens))

            for i, item in enumerate(lens):
                start = i - 1
                end = i - 1
                seq = lens2[end]

                if len(item) == int(lengthmax):
                    if i < 10:
                        ids = "%s%s%s" % (i, "-", item + "-")
                        ids = ids
                        ids = ids.replace(".", "")
                        ids = ids.replace("_", "")
                        print("1")
                    else:
                        ids = "%s%s%s" % (i, "-", item)
                        ids = ids
                        ids = ids.replace(".", "")
                        ids = ids.replace("_", "")
                        print("1")


                elif len(item) < int(lengthmax):
                    ids = "%s%s%s" % (i, "-", item)
                    add = int(lengthmax) - int(len(item))
                    ids = ids + (add * "-") + "-"
                    ids = ids
                    ids = ids.replace(".", "")
                    ids = ids.replace("_", "")
                    print("2")

                line = "%s          %s\n" % (ids.replace(".", ""), seq[0:100])
                print(line)
                file.write(line)
            file.close()


            # Read the sequences and align
            aln = AlignIO.read('phylo.phy', 'phylip')

            # Print the alignment
            print(aln)

            # Calculate the distance matrix
            calculator = DistanceCalculator('identity')
            dm = calculator.get_distance(aln)

            # Print the distance Matrix
            print('\nDistance Matrix\n===================')
            print(dm)

            # Construct the phylogenetic tree using UPGMA algorithm
            constructor = DistanceTreeConstructor()
            tree = constructor.upgma(dm)

            # Draw the phylogenetic tree
            Phylo.draw(tree)

            # Print the phylogenetic tree in the terminal
            print('\nPhylogenetic Tree\n===================')
            Phylo.draw_ascii(tree)
        win.quit()




        Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
        Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
        Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)
        mainloop()
    elif choice == "2":

        win = tk.Tk()
        sv1 = StringVar()
        sv2 = StringVar()
        Label(win, text="Input File").grid(row=0)
        Label(win, text="Output File").grid(row=1)

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

            records = SeqIO.parse("%s"%e1.get(), "fasta")

            lens = []
            lens2 = []
            file = open("phylo.phy", 'w')
            for record in records:
                ids = record.id
                sequence = record.seq[0:100]
                lens.append(record.id)
                lens2.append(record.seq)
                line = "%s   %s" % (ids, sequence)
                print(line)

            lengthmax = len(max(lens, key=len))

            lengthmin = len(min(lens, key=len))

            file.write("   %s     100\n" % len(lens))

            for i, item in enumerate(lens):
                start = i - 1
                end = i - 1
                seq = lens2[end]

                if len(item) == int(lengthmax):
                    if i < 10:
                        ids = "%s%s%s" % (i, "-", item + "-")
                        ids = ids
                        ids = ids.replace(".", "")
                        ids = ids.replace("_", "")
                        print("1")
                    else:
                        ids = "%s%s%s" % (i, "-", item)
                        ids = ids
                        ids = ids.replace(".", "")
                        ids = ids.replace("_", "")
                        print("1")


                elif len(item) < int(lengthmax):
                    ids = "%s%s%s" % (i, "-", item)
                    add = int(lengthmax) - int(len(item))
                    ids = ids + (add * "-") + "-"
                    ids = ids
                    ids = ids.replace(".", "")
                    ids = ids.replace("_", "")
                    print("2")

                line = "%s          %s\n" % (ids.replace(".", ""), seq[0:100])
                print(line)
                file.write(line)
            file.close()

            # Read the sequences and align
            aln = AlignIO.read('phylo.phy', 'phylip')

            # Print the alignment
            print(aln)

            # Calculate the distance matrix
            calculator = DistanceCalculator('identity')
            dm = calculator.get_distance(aln)

            # Print the distance Matrix
            print('\nDistance Matrix\n===================')
            print(dm)

            # Construct the phylogenetic tree using UPGMA algorithm
            constructor = DistanceTreeConstructor()
            tree = constructor.upgma(dm)

            Phylo.write(tree, 'apaf.xml', 'phyloxml')
            tree = Phylo.read('apaf.xml', 'phyloxml')
            Phylo.draw_graphviz(tree)
            pylab.show()

            win.destroy()

        Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
        Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
        Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

        mainloop()
    elif choice == "3":

        win = tk.Tk()
        sv1 = StringVar()
        sv2 = StringVar()
        Label(win, text="Input File").grid(row=0)
        Label(win, text="Output File").grid(row=1)

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

            records = SeqIO.parse("%s"%e1.get(), "fasta")

            lens = []
            lens2 = []
            file = open("phylo.phy", 'w')
            for record in records:
                ids = record.id
                sequence = record.seq[0:100]
                lens.append(record.id)
                lens2.append(record.seq)
                line = "%s   %s" % (ids, sequence)
                print(line)

            lengthmax = len(max(lens, key=len))

            lengthmin = len(min(lens, key=len))

            file.write("   %s     100\n" % len(lens))

            for i, item in enumerate(lens):
                start = i - 1
                end = i - 1
                seq = lens2[end]

                if len(item) == int(lengthmax):
                    if i < 10:
                        ids = "%s%s%s" % (i, "-", item + "-")
                        ids = ids
                        ids = ids.replace(".", "")
                        ids = ids.replace("_", "")
                        print("1")
                    else:
                        ids = "%s%s%s" % (i, "-", item)
                        ids = ids
                        ids = ids.replace(".", "")
                        ids = ids.replace("_", "")
                        print("1")


                elif len(item) < int(lengthmax):
                    ids = "%s%s%s" % (i, "-", item)
                    add = int(lengthmax) - int(len(item))
                    ids = ids + (add * "-") + "-"
                    ids = ids
                    ids = ids.replace(".", "")
                    ids = ids.replace("_", "")
                    print("2")

                line = "%s          %s\n" % (ids.replace(".", ""), seq[0:100])
                print(line)
                file.write(line)
            file.close()


            # Read the sequences and align
            aln = AlignIO.read('phylo.phy', 'phylip')

            # Print the alignment
            print(aln)

            # Calculate the distance matrix
            calculator = DistanceCalculator('identity')
            dm = calculator.get_distance(aln)

            # Print the distance Matrix
            print('\nDistance Matrix\n===================')
            print(dm)

            # Construct the phylogenetic tree using UPGMA algorithm
            constructor = DistanceTreeConstructor()
            tree = constructor.upgma(dm)

            Phylo.write(tree, 'apaf.xml', 'phyloxml')
            tree = Phylo.read('apaf.xml', 'phyloxml')
            net = Phylo.to_networkx(tree)
            networkx.draw_networkx(net)
            pylab.show(net)

        win.destroy()



        Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
        Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
        Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

        mainloop()


#allphylo("1")