# codonfreq . py
def CodonTable () :
    abet =  "acgt"
    answ = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                codon = abet[i] + abet[j] + abet[k]
                answ.append(codon)
    return answ



codons = CodonTable ()
print(len ( codons ))
print(codons [:4])




def ReadFile ( filename ) :
    fp = open(filename)
    data = fp.read()
    fp.close()
    return data




def GenomeCodonFreqs ( fname ) :

    data = ReadFile(fname)
    dna = ReadFile.ParseDNA(data)
    klocs = ReadFile.FindKeywordLocs(data)
    glocs = ReadFile.GeneLocs(data, klocs)
    frqs = []
    for g in glocs:
        cdna = ReadFile.GetCodingDNA(dna, g)
        if len(cdna) >= 192:
            f = CodonFreqs(cdna)
            frqs.append(f)
    return frqs


fname = "/home/peter/Desktop/Moduls/test_data/AF32668.gbk"
frqs =GenomeCodonFreqs ( fname )