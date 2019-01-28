paramters = {}
paramtersblast1 = {}
paramtergbkcon1 = {}
paramtergbkcon2 = {}
paramtergbkcon3 = {}
paramtergbkcon4 = {}
paramtergbkcon5 = {}
paramtergbkcon6 = {}
paramtergbkfname = {}
paramteriddatabase = {}
paramteropenneed = {}
paramterextendneed = {}
paramteropenwat = {}
paramterextendwat = {}
paramterglobalopen = {}
paramterglobalexten = {}
paramterlocalopen = {}
paramterlocalexten = {}
paramterpammat = {}
paramterpammode = {}
paramterpamopen = {}
paramterpamextend = {}
paramterblosummat = {}
paramterblosummode = {}
paramterblosumopen = {}
paramterblosumextend = {}
paramterweblogo = {}
paramterchrom = {}
paramterdowndb = {}
paramterdowntype = {}
paramterphylo = {}
paramterorf = {}








textboxes = []

paramters["protable"]="Standard"
paramters["prostop"]="1"

paramtersblast1["blastdb"] = 'Nucleotide collection(DNA)'
paramtersblast1["blastalign"] = "1"
paramtersblast1["blastprog"] = "BLASTn"

paramtergbkcon1["gene"] = True
paramtergbkcon2["product"] = True
paramtergbkcon3["protein"] = True
paramtergbkcon4["codonstart"] = True
paramtergbkcon5["translation"] = True
paramtergbkcon6["transaltiontable"] = True
paramtergbkfname["filename"] = '1'

paramteriddatabase["1"] = 'nucleotide'
paramteriddatabase["2"] = 'fasta'

paramteropenneed["open"] = '-11'
paramterextendneed["extend"] = '-1'

paramterglobalopen["open"] = '-11'
paramterglobalexten["extend"] = '-1'

paramterlocalopen["open"] = '-11'
paramterlocalexten["extend"] = '-1'

paramterpammat['matrix'] = 'PAM 250'
paramterpammode['mode'] ="Global"
paramterpamopen['open']= '-11'
paramterpamextend['extend']= '-1'

paramterblosummat['matrix'] = 'BLOSUM 62'
paramterblosummode['mode'] ="Global"
paramterblosumopen['open']= '-11'
paramterblosumextend['extend']= '-1'

paramterweblogo['length'] = '100'

paramterchrom['type'] = "1"

paramterdowndb ['database'] = 'nucleotide'
paramterdowntype ['type'] = 'fasta'

paramterphylo['type']="1"


paramterphylo['type']="1"



from tkinter import ttk
from functions.translation import *
from functions.GC import *
from functions.transcrip import *
from functions.backtranscripe import *
from functions.reverscomplement import *
from functions.genbank_extractio_multiple import *
from functions.genbank_extraction_one import *
from functions.search_id import *
from functions.transcription_IDs_list import *
from functions.reverscomplement_IDs_list import *
from functions.translat_IDs_list import *
from functions.GC_content_IDs_list import *
from functions.Nucglob_alignment import *
from functions.Nucloc_Alignment import *
from functions.blastid import *
from functions.pubmed import *
from functions.needleman_alignment import *
from functions.water_alignment import *
from functions.dotplot import *
from functions.restrict_sites import *
from functions.trim_adaptor import *
from functions.trim_primer import *
from functions.gc_graphic import *
from functions.BLOSUM_Alignment import *
from functions.pam_alignment import *
from functions.weblogo import *
from functions.tree import *
from functions.BLAST import *
from functions.translat_IDs_list import *
from functions.download_records import *
from functions.orf import *
from functions.back_transcrip_ids import *
from functions.IDs_orf import *
from functions.all_phylogenetic import *
from functions.back_transcrip_ids import *
from functions.chromosome import *
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import os


import easygui



root = tk.Tk()


c1=tk.BooleanVar()
c2=tk.BooleanVar()
c3=tk.BooleanVar()
c4=tk.BooleanVar()
c5=tk.BooleanVar()
c6=tk.BooleanVar()
v = StringVar()
v.set(0)




ndl = StringVar()
ndl.set(1)


style = ttk.Style()
mygreen = "#d2ffd2"
myred = "#dd0202"
style.theme_create( "GUI", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": myred },
            "map":       {"background": [("selected", myred)],
                          "expand": [("selected", [5, 5, 5, 5])] } } } )

COLOR_1 = 'black'
COLOR_2 = 'white'
COLOR_3 = 'red'
COLOR_4 = '#d9d9d9'
COLOR_5 = '#8A4B08'
COLOR_6 = '#D9D9D9'

noteStyler = ttk.Style()
noteStyler.configure("TNotebook", background=COLOR_6, borderwidth=0)
noteStyler.configure("TNotebook.Tab", background=COLOR_1, foreground=COLOR_3, lightcolor=COLOR_2, borderwidth=3)
noteStyler.configure("TFrame", background=COLOR_4, foreground=COLOR_3, borderwidth=1000)


style = ttk.Style(root)
style.configure('toptab.TNotebook', tabposition='wn')
root.resizable(0,0)
root.title("Bio-STAMP")



tabControl = ttk.Notebook(root)


tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Nucleotide')
tabControl.pack(expand=1, fill="both")
f = Frame(tab1, width=700, height=110)
frame1 = Frame(f, relief=RAISED, borderwidth=5)
frame1.grid(row = 1 , column=0 , pady=15)
Label(f,text ='FASTA File', font='bold').grid(row = 0 , column=0)
f.pack()

frame2 = Frame(f, relief=RAISED, borderwidth=5)
frame2.grid(row = 3 , column=0 , pady=15)
Label(f, text='IDs LIST' , font='bold').grid(row = 2 , column=0)





tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='DATA Extraction')
tabControl.pack(expand=1, fill="both")
fd = Frame(tab2, width=5, height=110)
framed = Frame(fd, relief=GROOVE, borderwidth=5)
framed.grid(row = 1 , column=0 , pady=5, padx=0)
fd.grid(row=1)



tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='BLAST')
tabControl.pack(expand=100, fill="x")


f3 = Frame(tab3, width=700, height=110)
frame3 = Frame(f3, relief=GROOVE, borderwidth=5)
frame3.grid(row = 1 , column=0 , pady=5, padx=100)
f3.grid(row=1)
Label(f3, text='↓BLAST↓' , font='bold').grid(row = 0 , column=0)

f4 = Frame(tab3, width=700, height=110)
frame4 = Frame(f4, relief=GROOVE, borderwidth=5)
frame4.grid(row = 1 , column=0 , pady=5)
f4.grid(row=2)
Label(f4, text='ID Search' , font='bold').grid(row = 0 , column=0)


f5 = Frame(tab3, width=700, height=110)
frame5 = Frame(f5, relief=GROOVE, borderwidth=5)
frame5.grid(row = 2 , column=0 , pady=5)
f5.grid(row=3)
Label(f5, text='Query Search' , font='bold').grid(row = 0 , column=0)


tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='Alignment')
tabControl.pack(expand=1, fill="both")

tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text='Quality Control')
tabControl.pack(expand=1, fill="both")

tab6 = ttk.Frame(tabControl)
tabControl.add(tab6, text='Visualization')
tabControl.pack(expand=1, fill="both")

f6 = Frame(tab6, width=700, height=110)
frame6 = Frame(f6, relief=GROOVE, borderwidth=5)
frame6.grid(row = 1 , column=1)
f6.grid(row=1)
Label(f6, text='PhyloGenetic' , font='bold').grid(row =0 , column=1)



menubar = Menu(root)

def aboutoz():
    root1 = tk.Toplevel()
    root1.title("Bio-STAMP")
    logo = tk.PhotoImage(file="/home/peter/Downloads/ICARDA_logo_square (2).gif")
    root1.resizable(0, 0)

    w1 = tk.Label(root1, image=logo).pack(side="right")

    explanation = "Bio-STAMP\nVersion 0.1 2018/2019\nFor More Information:\nE-mail: p.habib911@gmail.com\n              Samman.Mahmoud@gmail.com\n              a.hamwieh@cgiar.org "

    w2 = tk.Label(root1,
                  justify=tk.LEFT,
                  padx=10,
                  text=explanation , font=('helvetica', 12, 'bold')).pack(side="left")
    root1.mainloop()
def opentrans():


    root2 = tk.Tk()

    label = tk.Label(root2, text="Codon Tables:", fg='red', font=('Ubuntu Medium', 9, 'bold'))
    label.grid(row=0, column=0)

    OPTIONS = ["Standard", "Vertebrate Mitochondrial", "Yeast Mitochondrial",
               "Mold Mitochondrial; Protozoan Mitochondrial; Coelenterate Mitochondrial; Mycoplasma; Spiroplasma",
               "Invertebrate Mitochondrial", "Ciliate Nuclear; Dasycladacean Nuclear; Hexamita Nuclear",
               "Echinoderm Mitochondrial; Flatworm Mitochondrial", "Euplotid Nuclear",
               "Bacterial, Archaeal and Plant Plastid", "Alternative Yeast Nuclear", "Ascidian Mitochondrial",
               "Alternative Flatworm Mitochondrial", "Blepharisma Macronuclear", "Chlorophycean Mitochondrial",
               "Trematode Mitochondrial", "Scenedesmus obliquus Mitochondrial", "Thraustochytrium Mitochondrial",
               "Pterobranchia Mitochondrial", "Candidate Division SR1 and Gracilibacteria",
               "Pachysolen tannophilus Nuclear", "Karyorelict Nuclear", "Condylostoma Nuclear", "Mesodinium Nuclear",
               "Peritrich Nuclear", "Blastocrithidia Nuclear"]
    table = StringVar(root2)
    table.set(OPTIONS[0])  # default value
    w = OptionMenu(root2, table, *OPTIONS)
    w.grid(row=0, column=1)

    tostop = IntVar()
    tostop.set(0)
    chb = Checkbutton(root2, text="Stop Translate at\nFirst Stop Codon", variable=tostop)
    chb.grid(row=0,column=2)


    def write():
        paramters["protable"] ="%s"% table.get()
        paramters["prostop"] ="%s"% tostop.get()
        root2.destroy()

    button = Button(root2, text='OK' , command = write)
    button.grid(row=2, column=0, sticky=W, pady=0)
    button.config(font=('Ubuntu Medium', 9, 'bold'))
def blastmenu():
    root3 = tk.Tk()

    label = tk.Label(root3, text="Program")
    label.grid(row=1, column=0)
    label.config(font=('helvetica', 10, 'bold'))

    blast = ['BLASTn', 'BLASTp', 'BLASTx', 'tBLASTn', 'tBLASTx']
    value = StringVar(root3)
    value.set(blast[0])
    w = OptionMenu(root3, value, *blast)
    w.grid(row=1, column=1)

    label = tk.Label(root3, text="DataBase")
    label.grid(row=0, column=0)
    label.config(font=('helvetica', 10, 'bold'))

    database = ['Nucleotide collection(DNA)', 'NCBI Transcript Ref_Seq Database(DNA)', 'PDB Nucleotide DataBase(DNA)',
                'Non-redundant(Protein)', 'NCBI Protein Reference Sequences(Protein)',
                'Non-redundant UniProtKB/SwissProt sequences(Protein)', 'Expressed Sequences tags(DNA)',
                'RefSeq Representative Genome Database(DNA)']
    valdb = StringVar(root3)
    valdb.set(database[0])  # default value
    w = OptionMenu(root3, valdb, *database)
    w.grid(row=0, column=1)
    valdb.trace('w', change_dropdown)

    alignz = IntVar()
    alignz.set(0)
    chb = Checkbutton(root3, text="Show Alignmnet", variable=alignz)
    chb.grid(row=1, column=2)

    def endblast():
        paramtersblast1["blastdb"] ="%s"% valdb.get()
        paramtersblast1["blastalign"] = "%s"%alignz.get()
        paramtersblast1["blastprog"] = "%s"%value.get()
        root3.destroy()

    button = Button(root3, text='OK', command=endblast)
    button.grid(row=2, column=1)
    button.config(font=('Ubuntu Medium', 9, 'bold'))
def gbk():
    root4 = tk.Tk()
    f = Frame(root4, width=300, height=110)
    frame1 = Frame(f, relief=GROOVE, borderwidth=5)
    frame1.grid(row=1, column=0, pady=15)
    Label(f, text='File Content', font='bold').grid(row=0, column=0)
    f.pack()

    cb1 = tk.Checkbutton(frame1, text='    Gene     ', variable=c1)
    cb1.grid(row=3, column=0)
    cb2 = tk.Checkbutton(frame1, text='   Product  ', variable=c2)
    cb2.grid(row=4, column=0)
    cb3 = tk.Checkbutton(frame1, text=' Protein id  ', variable=c3)
    cb3.grid(row=5, column=0)
    cb4 = tk.Checkbutton(frame1, text='Codon Start', variable=c4)
    cb4.grid(row=6, column=0)
    cb5 = tk.Checkbutton(frame1, text=' Translation', variable=c5)
    cb5.grid(row=7, column=0)
    cb6 = tk.Checkbutton(frame1, text=' Translation\nTables', variable=c6)
    cb6.grid(row=8, column=0)

    frame2 = Frame(f, relief=GROOVE, borderwidth=5)
    frame2.grid(row=1, column=1, pady=15)
    Label(f, text='File Name', font='bold').grid(row=0, column=1)


    rb1 = tk.Radiobutton(frame2, text='    Gene     ', variable=v, value=1)
    rb1.grid(row=3, column=0)
    rb2 = tk.Radiobutton(frame2, text='   Product  ', variable=v, value=2)
    rb2.grid(row=4, column=0)
    rb3 = tk.Radiobutton(frame2, text=' Protein id  ', variable=v, value=3)
    rb3.grid(row=5, column=0)
    rb4 = tk.Radiobutton(frame2, text='Codon Start', variable=v, value=4)
    rb4.grid(row=6, column=0)
    rb5 = tk.Radiobutton(frame2, text=' Translation', variable=v, value=5)
    rb5.grid(row=7, column=0)
    rb6 = tk.Radiobutton(frame2, text=' Translation\nTables', variable=v, value=6)
    rb6.grid(row=8, column=0)

    def endgbk():
        paramtergbkcon1["gene"] = "%s"%c1.get()
        paramtergbkcon2["product"] ="%s"% c2.get()
        paramtergbkcon3["protein"] ="%s"% c3.get()
        paramtergbkcon4["codonstart"] = "%s"%c4.get()
        paramtergbkcon5["translation"] ="%s"% c5.get()
        paramtergbkcon6["transaltiontable"] ="%s"% c6.get()
        paramtergbkfname["filename"] = v.get()
        root4.destroy()

    button = Button(root4, text='OK', command=endgbk)
    button.pack()
    button.config(font=('Ubuntu Medium', 9, 'bold'))
def searchpara():
    root5 = tk.Tk()

    Label(root5, text="DataBase").grid(row=0)
    OPTIONS = ["gene", "genome", "Protein", "nucleotide"]
    variable = StringVar(root5)
    variable.set(OPTIONS[0])  # default value
    w = OptionMenu(root5, variable, *OPTIONS)
    w.grid(row = 0 , column = 1)

    Label(root5, text="Output Type").grid(row=1)
    types = ["gb", "fasta"]
    type = StringVar(root5)
    type.set(types[0])  # default value
    w = OptionMenu(root5, type, *types)
    w.grid(row = 1 , column = 1)


    def endsearch():
        paramteriddatabase["1"] ="%s"% variable.get()
        paramteriddatabase["2"] ="%s"% type.get()

        root5.destroy()


    button = Button(root5, text='OK', command=endsearch)
    button.grid(row = 2 , column = 0)
    button.config(font=('Ubuntu Medium', 9, 'bold'))
def needwat():

    def write():
        paramteropenneed["open"] = "%s"%e1.get()
        paramterextendneed["extend"] ="%s"% e2.get()
        master.destroy()


    master = Tk()
    Label(master, text="First Name").grid(row=0)
    Label(master, text="Last Name").grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Show', command=write).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()
def glob():


    def write():
        paramterglobalopen["open"] = "%s"%e1.get()
        paramterglobalexten["extend"] ="%s"% e2.get()
        master.destroy()


    master = Tk()
    Label(master, text="Gap Opening").grid(row=0)
    Label(master, text="Gap Extention").grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='OK', command=write).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()
def loc():


    def write():
        paramterlocalopen["open"] = "%s"%e1.get()
        paramterlocalexten["extend"] = "%s"%e2.get()
        master.destroy()


    master = Tk()
    Label(master, text="Gap Opening").grid(row=0)
    Label(master, text="Gap Extention").grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='OK', command=write).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()
def pampara():
    root5 = tk.Tk()

    Label(root5, text="Matrix").grid(row=0)
    OPTIONS = ["PAM 300","PAM 250","PAM 180","PAM 120","PAM 90","PAM 60","PAM 30"]
    variable = StringVar(root5)
    variable.set(OPTIONS[1])  # default value
    w = OptionMenu(root5, variable, *OPTIONS)
    w.grid(row = 0 , column =2)

    Label(root5, text="Type").grid(row=1)
    types = ["Local", "Global"]
    type = StringVar(root5)
    type.set(types[1])  # default value
    w = OptionMenu(root5, type, *types)
    w.grid(row = 1 , column = 2)

    Label(root5, text="Gap Opening").grid(row=0)
    Label(root5, text="Gap Extention").grid(row=1)

    e1 = Entry(root5)
    e2 = Entry(root5)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)


    def endsearch():
        paramterpammat['matrix'] ="%s"% variable.get()
        paramterpammode['mode'] = "%s"%type.get()
        paramterpamopen['open']= "%s"%e1.get()
        paramterpamextend['extend']="%s"%e2.get()

        root5.destroy()


    button = Button(root5, text='OK', command=endsearch)
    button.grid(row = 2 , column = 0)
    button.config(font=('Ubuntu Medium', 9, 'bold'))
def blosumpara():
    root5 = tk.Tk()

    Label(root5, text="Matrix").grid(row=0)
    OPTIONS = ["BLOSUM 30","BLOSUM 35","BLOSUM 40","BLOSUM 45","BLOSUM 50","BLOSUM 55","BLOSUM 60","BLOSUM 62","BLOSUM 65","BLOSUM 70","BLOSUM 75","BLOSUM 80","BLOSUM 85","BLOSUM 90","BLOSUM 95","BLOSUM 100"]
    variable = StringVar(root5)
    variable.set(OPTIONS[1])  # default value
    w = OptionMenu(root5, variable, *OPTIONS)
    w.grid(row = 0 , column =2)

    Label(root5, text="Type").grid(row=1)
    types = ["Local", "Global"]
    type = StringVar(root5)
    type.set(types[1])  # default value
    w = OptionMenu(root5, type, *types)
    w.grid(row = 1 , column = 2)

    Label(root5, text="Gap Opening").grid(row=0)
    Label(root5, text="Gap Extention").grid(row=1)

    e1 = Entry(root5)
    e2 = Entry(root5)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)


    def endsearch():
        paramterblosummat['matrix'] ="%s"% variable.get()
        paramterblosummode['mode'] ="%s"% type.get()
        paramterblosumopen['open']="%s"% e1.get()
        paramterblosumextend['extend']="%s"%e2.get()

        root5.destroy()


    button = Button(root5, text='OK', command=endsearch)
    button.grid(row = 2 , column = 0)
    button.config(font=('Ubuntu Medium', 9, 'bold'))
def webpara():

    def write():
        paramterweblogo['length'] ="%s"% e1.get()
        master.destroy()


    master = Tk()
    Label(master, text="Length").grid(row=0)


    e1 = Entry(master)


    e1.grid(row=0, column=1)


    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='OK', command=write).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()
def parachrom():

    def write():
        paramterchrom['type'] ="%s"% v.get()
        master.destroy()


    master = Tk()
    rb11 = tk.Radiobutton(master, text='    Gene     ', variable=v, value=1)
    rb11.grid(row=0, column=0)
    rb22 = tk.Radiobutton(master, text='    tRNA     ', variable=v, value=2)
    rb22.grid(row=1, column=0)
    rb33 = tk.Radiobutton(master, text='    mRNA     ', variable=v, value=3)
    rb33.grid(row=2, column=0)


    Button(master, text='Quit', command=master.quit).grid(row=3, column=0)
    Button(master, text='OK', command=write).grid(row=3, column=1)

    mainloop()
def blosumpara():
    root5 = tk.Tk()

    Label(root5, text="DataBase").grid(row=0)
    OPTIONS = ['nucleotide' , 'gene' , 'protein']
    variabledb = StringVar(root5)
    variabledb.set(OPTIONS[1])  # default value
    w = OptionMenu(root5, variabledb, *OPTIONS)
    w.grid(row = 0 , column =2)

    Label(root5, text="Type").grid(row=1)
    types = ["fasta", "gb"]
    typedb = StringVar(root5)
    typedb.set(types[1])  # default value
    w = OptionMenu(root5, typedb, *types)
    w.grid(row = 1 , column = 2)


    def endsearch():
        paramterdowndb['database'] ="%s"% variabledb.get()
        paramterdowntype ['type'] ="%s"% typedb.get()


        root5.destroy()


    button = Button(root5, text='OK', command=endsearch)
    button.grid(row = 2 , column = 0)
    button.config(font=('Ubuntu Medium', 9, 'bold'))
def paraphylo():
    root = tk.Toplevel()

    v = tk.IntVar()

    def write():
        paramterphylo['type'] = "%s"%v.get()
        print(paramterphylo['type'])
        root.destroy()




    rb11 = tk.Radiobutton(root, text='    Tree      ', variable=v, value=1)
    rb11.grid(row=0, column=0)
    rb22 = tk.Radiobutton(root, text='Network 1', variable=v, value=2)
    rb22.grid(row=1, column=0)
    rb33 = tk.Radiobutton(root, text='Network 2', variable=v, value=3)
    rb33.grid(row=2, column=0)


    Button(root, text='Quit', command=root.quit).grid(row=3, column=0)
    Button(root, text='OK', command=write).grid(row=3, column=1)

    mainloop()
def orfids():


    def write():
        paramterlocalopen["open"] = "%s"%e1.get()
        paramterlocalexten["extend"] = "%s"%e2.get()
        master.destroy()


    master = Tk()
    Label(master, text="Gap Opening").grid(row=0)
    Label(master, text="Gap Extention").grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='OK', command=write).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()




def prot():
    protein(paramters["protable"],paramters["prostop"])
def gc():
    gccontent()
    print("DONE!")
def trans():
    transcrib()
    print("DONE!")
def bktrans():
    bktranscrip()
def revr():
    revcom()
def rgbtrans():
    multigbk(c1.get(), c2.get(), c3.get(), c4.get(), c5.get(), c6.get(), v.get())
def rgl():
    onegbk()
def sr4():
    search(paramteriddatabase["1"], paramteriddatabase["2"], "%s"% e2id.get())
def transcribids():
    transcids()
def revcompids():
    revcomids2()
def translatids():
    translids(paramters["protable"], paramters["prostop"])
def gcids():
    gccontentids()
def srch():
    blast(paramtersblast1["blastprog"],paramtersblast1["blastdb"], paramtersblast1["blastalign"])
def openblast():
    openblasts(paramtersblast1["blastprog"],paramtersblast1["blastdb"], paramtersblast1["blastalign"])
def gloms():
    glomsalign(paramterglobalopen['open'] , paramterglobalexten['extend'])
def local():
    locals(paramterlocalopen['open'], paramterlocalexten['extend'])
def pub():
    pubm("%s" % e4qu.get())
def nmw():
    nmwneedle(paramteropenneed["open"], paramterextendneed["extend"])
def nmw2():
    nmwwater(paramteropenneed["open"], paramterextendneed["extend"])
def sra():
    dplot()
def pls():
    ressites()
def tprim():
    tprimer()
def fastofasq():
    fastofasq()
def tadopt():
    tadoptor()
def gcs():
    gcsgraph()
def pamall():
    pamalign(paramterpammat['matrix'], paramterpammode['mode'],int(paramterpamopen['open']),int(paramterpamextend['extend']))
def blosumall():
    blosumalign(paramterblosummat['matrix'],paramterblosummode['mode'], int(paramterblosumopen['open']), int(paramterblosumextend['extend']))
def tree():
    treedrawing()
def webl():
    weblogo(paramterweblogo['length'])
def Chrom():
    Chromsome(paramterchrom['type'])
def recget():
    download(paramterdowndb['database'], paramterdowntype['type'])
def recgetsep():
    download(paramterdowndb['database'], paramterdowntype['type'])
def openrf():
    opffile("Standard" , '-1')
def backids():
    bacsids()
def openrfids():
    opf("Standard" , '-1')
def phy1o1():
    allphylo(paramterphylo['type'])



####################################################### TAB 1 #########################################################



button2 = tk.Button(frame1, text='  Translation ', command=prot, font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)
button2.grid(row=0 , column= 0, padx=20,pady=10)

button1 = tk.Button(frame1, text='Transcription', command=trans, font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)
button1.grid(row=1 , column= 0, padx=20,pady=10)


button3 = tk.Button(frame1, text=' Revrse\nComplement ', command=revr , font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)
button3.grid(row=0 , column= 2, padx=20,pady=10)



button4 = tk.Button(frame1, text='   GC% Contet   ', command=gc , font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)
button4.grid(row=0 , column= 1, padx=20,pady=10)


button5 = tk.Button(frame1, text='Back \nTranscription', command=bktrans , font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)
button5.grid(row=1 , column= 1, padx=20,pady=10)

button5 = tk.Button(frame1, text='Open Reading\nFrame', command=openrf , font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)
button5.grid(row=1 , column= 2, padx=20,pady=10)

button18 = Button(frame2, text='IDs Translation', command=translatids)
button18.grid(row=0, column=0, padx=20,pady=5)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button18 = Button(frame2, text='IDs Transcription', command=transcribids)
button18.grid(row=1, column=1, padx=20,pady=5)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button18 = Button(frame2, text='''IDs Reverse
complement''', command=revcompids)
button18.grid(row=0, column=1, padx=20,pady=5)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button18 = Button(frame2, text='IDs GC% Content', command=gcids)
button18.grid(row=0, column=2, padx=20,pady=5)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)

button18 = Button(frame2, text='IDs Back \nTranscription', command=backids)
button18.grid(row=1, column=2, padx=20,pady=5)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button18 = Button(frame2, text='IDs Open\nReading Frames', command=openrfids)
button18.grid(row=1, column=0, padx=20,pady=5)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


####################################################### TAB 2 #########################################################

button5 = Button(framed, text='''Extraction In\nMultiple Files''', command=rgbtrans)
button5.grid(row=2, column=0, pady=10, padx=10)
button5.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)

button7 = Button(framed, text='''Extraction In \none Files''', command=rgl)
button7.grid(row=2, column=1, pady=10, padx=10)
button7.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)

frame1 = Frame(framed, relief=SUNKEN, borderwidth=5)
frame1.grid(row=1, column=0)
Label(framed, text='File Content', font='bold').grid(row=0, column=0)
f.pack()

cb1 = tk.Checkbutton(frame1, text='    Gene     ', variable=c1)
cb1.grid(row=3, column=0)
cb2 = tk.Checkbutton(frame1, text='   Product  ', variable=c2)
cb2.grid(row=4, column=0)
cb3 = tk.Checkbutton(frame1, text=' Protein id  ', variable=c3)
cb3.grid(row=5, column=0)
cb4 = tk.Checkbutton(frame1, text='Codon Start', variable=c4)
cb4.grid(row=6, column=0)
cb5 = tk.Checkbutton(frame1, text=' Translation', variable=c5)
cb5.grid(row=7, column=0)
cb6 = tk.Checkbutton(frame1, text=' Translation\nTables', variable=c6)
cb6.grid(row=8, column=0)

frame2 = Frame(framed, relief=SUNKEN, borderwidth=5)
frame2.grid(row=1, column=1)
Label(framed, text='File Name', font='bold').grid(row=0, column=1)

rb1 = tk.Radiobutton(frame2, text='    Gene     ', variable=v, value=1)
rb1.grid(row=3, column=0)
rb2 = tk.Radiobutton(frame2, text='   Product  ', variable=v, value=2)
rb2.grid(row=4, column=0)
rb3 = tk.Radiobutton(frame2, text=' Protein id  ', variable=v, value=3)
rb3.grid(row=5, column=0)
rb4 = tk.Radiobutton(frame2, text='Codon Start', variable=v, value=4)
rb4.grid(row=6, column=0)
rb5 = tk.Radiobutton(frame2, text=' Translation', variable=v, value=5)
rb5.grid(row=7, column=0)
rb6 = tk.Radiobutton(frame2, text=' Translation\nTables', variable=v, value=6)
rb6.grid(row=8, column=0)



button7 = Button(tab2, text='''Download Records \nin one file''', command=recget)
button7.grid(row=3, column=0, pady=25, padx=200)
button7.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)

button7 = Button(tab2, text='''Download Records \nin Multiple files''', command=recgetsep)
button7.grid(row=4, column=0, pady=25, padx=200)
button7.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


####################################################### TAB 3 #########################################################


Label(frame4, text="Enter ID:").grid(row=0)
e2id = Entry(frame4)
e2id.grid(row=0, column=1 , pady = 10,padx=10)

Label(frame5, text="Enter Query:").grid(row=0)
e4qu = Entry(frame5)
e4qu.grid(row=0, column=1, pady = 10,padx=10)


button11 = Button(frame5, text='Search', command=pub)
button11.grid(row=1, column=0, sticky=W, padx=30 , pady=10)
button11.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)

button9 = Button(frame4, text='Search', command=sr4)
button9.grid(row=1, column=0, sticky=W, padx=30 , pady=10)
button9.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)

button10 = Button(frame3, text='Sequence BLAST', command=srch)
button10.grid(row=2, column=0, sticky=W, padx=10 , pady=10)
button10.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button11 = Button(frame3, text='   ID BLAST   ', command=openblast)
button11.grid(row=2, column=1, sticky=W, padx=10 , pady=10)
button11.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)





####################################################### TAB 4 #########################################################

button15 = Button(tab4, text=' BLOSUM Alignment',command=blosumall)
button15.grid(row=0, column=0, sticky=W, padx=50 , pady=25)
button15.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button15 = Button(tab4, text='   PAM Alignment    ', command = pamall)
button15.grid(row=0, column=1, sticky=W, padx=50 , pady=25)
button15.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button13 = Button(tab4, text='  Global Alignment  ', command=gloms)
button13.grid(row=1, column=0, sticky=W, padx=50 , pady=25)
button13.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button15 = Button(tab4, text='   Local Alignment   ', command=local)
button15.grid(row=1, column=1, sticky=W, padx=50 , pady=25)
button15.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button14 = Button(tab4, text='       Needleman       ', command=nmw)
button14.grid(row=2, column=0, sticky=W, padx=50 , pady=25)
button14.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button14 = Button(tab4, text='           Water           ', command=nmw2)
button14.grid(row=2, column=1, sticky=W, padx=50 , pady=25)
button14.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


####################################################### TAB 5 #########################################################

button18 = Button(tab5, text='  Trimming Primer  ', command=tprim , font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)
button18.grid(row=0, column=0, sticky=W, padx=170 , pady=25)


button18 = Button(tab5, text='    FastQ To Fasta    ', command=fastofasq)
button18.grid(row=1,column=0,sticky=W, padx=170 , pady=25)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)



button18 = Button(tab5, text=' Trimming Adaptors ', command=tadopt)
button18.grid(row=2,column=0,sticky=W, padx=170 , pady=25)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


####################################################### TAB 6 #########################################################


button17 = Button(tab6, text='    Chromosome    ', command=Chrom)
button17.grid(row=2, column=0, sticky=W, padx=50 , pady = 25)
button17.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button16 = Button(tab6, text='         Dotplot         ', command=sra)
button16.grid(row=4, column=0, sticky=W, padx = 50 , pady = 25)
button16.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button17 = Button(tab6, text='   Restriction sites  ', command=pls)
button17.grid(row=3, column=1, sticky=W, padx = 50 , pady = 25)
button17.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button18 = Button(tab6, text='    GC% Content     ', command=gcs)
button18.grid(row=3, column=0, sticky=W, padx = 50 , pady = 25)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)

button18 = Button(tab6, text='Phylogenetic Tree ', command=phy1o1)
button18.grid(row=4, column=1, sticky=W, padx = 50 , pady = 25)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)


button18 = Button(tab6, text='        Weblogo        ', command=webl)
button18.grid(row=2, column=1, sticky=W , padx = 50 , pady = 25)
button18.config(font=('Times Roman', 10, 'bold'), fg='white', bg='black',  bd=10)







filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",font=('Times Roman', 10, 'bold') )
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", font=('Times Roman', 10, 'bold') , menu = filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About..." ,font=('Times Roman', 10, 'bold'), command=aboutoz)
menubar.add_cascade(label="Help",font=('Times Roman', 10, 'bold'), menu=helpmenu)


paramenu = Menu(menubar, tearoff=0)
paramenu2= Menu(paramenu, tearoff=0)

paramenu2.add_command(label="Translation" ,font=('Times Roman', 10, 'bold'), command = opentrans)
paramenu2.add_command(label="Translation IDs" ,font=('Times Roman', 10, 'bold'), command = opentrans)
#paramenu2.add_command(label='Open Reading Frame IDs' ,font=('Times Roman', 10, 'bold'), command = ofrids)
paramenu.add_cascade(label="Nucleotide",font=('Times Roman', 10, 'bold'), menu=paramenu2)

parablast= Menu(paramenu, tearoff=0)
parablast.add_command(label="BLAST" ,font=('Times Roman', 10, 'bold'), command = blastmenu)
paramenu.add_cascade(label="Search",font=('Times Roman', 10, 'bold'), menu=parablast)

paragbk= Menu(paramenu, tearoff=0)
paragbk.add_command(label="Extraction" ,font=('Times Roman', 10, 'bold'), command = gbk)
paramenu.add_cascade(label="GBK",font=('Times Roman', 10, 'bold'), menu=paragbk)

parasearch= Menu(paramenu, tearoff=0)
parasearch.add_command(label="Option" ,font=('Times Roman', 10, 'bold'), command = searchpara)
paramenu.add_cascade(label="Search",font=('Times Roman', 10, 'bold'), menu=parasearch)

parasearch= Menu(paramenu, tearoff=0)
parasearch.add_command(label="Chromosome" ,font=('Times Roman', 10, 'bold'), command = parachrom)
parasearch.add_command(label="PhyloGenetic Tree" ,font=('Times Roman', 10, 'bold'), command = paraphylo)
paramenu.add_cascade(label="Visualization",font=('Times Roman', 10, 'bold'), menu=parasearch)


paraalign= Menu(paramenu, tearoff=0)
paraprot = Menu(paraalign, tearoff=0)
paranuc = Menu(paraalign, tearoff=0)
paranuc.add_command(label="Needleman" ,font=('Times Roman', 10, 'bold'), command = needwat)
paranuc.add_command(label="Water" ,font=('Times Roman', 10, 'bold'), command = needwat)
paranuc.add_command(label="Global" ,font=('Times Roman', 10, 'bold'), command = glob)
paranuc.add_command(label="Local" ,font=('Times Roman', 10, 'bold'), command = loc)
paraprot.add_command(label="BLOSUM" ,font=('Times Roman', 10, 'bold'),command = pampara)
paraprot.add_command(label="    PAM" ,font=('Times Roman', 10, 'bold'), command = blosumpara)

paraalign.add_cascade(label="Protein",font=('Times Roman', 10, 'bold'), menu=paraprot)
paraalign.add_cascade(label="Nucleotide",font=('Times Roman', 10, 'bold'), menu=paranuc)
paramenu.add_cascade(label="Alignment",font=('Times Roman', 10, 'bold'), menu=paraalign)
menubar.add_cascade(label="Parameters",font=('Times Roman', 10, 'bold'), menu=paramenu)


root.config(menu=menubar)

root.mainloop()

