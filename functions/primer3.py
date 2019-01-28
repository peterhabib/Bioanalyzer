from Bio.Emboss.Applications import Primer3Commandline
cline = Primer3Commandline(sequence="mysequence.fas", auto=True, hybridprobe=True)
cline.explainflag = True
cline.oligosize=20              # Old EMBOSS, instead of osizeopt
cline.productosize=200          # Old EMBOSS, instead of psizeopt
cline.outfile = "myresults.txt"
print(cline)
