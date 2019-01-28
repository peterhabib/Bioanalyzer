from Bio import SeqIO
from Bio.Graphics import GenomeDiagram
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.SeqFeature import SeqFeature, FeatureLocation
from tkinter import filedialog
from tkinter import *
import tkinter as tk

def ressites():
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
        record = SeqIO.read(infile, "genbank")

        gd_diagram = GenomeDiagram.Diagram(record.id)
        gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
        gd_feature_set = gd_track_for_features.new_set()

        for feature in record.features:
            if feature.type != "gene":
                continue
            if len(gd_feature_set) % 2 == 0:
                color = colors.blue
            else:
                color = colors.lightblue
            gd_feature_set.add_feature(feature, sigil="ARROW", color=color, label=True, label_size=10,
                                       label_angle=0)

        for site, name, color in [("GAATTC", "EcoRI", colors.green), ("CCCGGG", "SmaI", colors.orange),
                                  ("AAGCTT", "HindIII", colors.red), ("GGATCC", "BamHI", colors.purple)]:

            index = 0
            while True:
                index = record.seq.find(site, start=index)
                if index == -1: break
                feature = SeqFeature(FeatureLocation(index, index + len(site)))
                gd_feature_set.add_feature(feature, color=color, name=name, label=True, label_size=10,
                                           label_color=color)
                index += len(site)

        gd_diagram.draw(format="linear", pagesize='A4', fragments=1, start=0, end=len(record), orientation='landscape',
                        tracklines=0, circular=5)
        gd_diagram.write("plasmid_linear_nice.pdf", "PDF")

        gd_diagram.draw(format="circular", circular=True, pagesize=(20 * cm, 20 * cm), start=0, end=len(record),
                        circle_core=1.2)

        gd_diagram.write("plasmid_circular_nice.pdf", "PDF")




        win.destroy()



    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()



