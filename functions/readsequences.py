from Bio import SeqIO
def readphylo():
    records = SeqIO.parse("/home/peter/Desktop/Moduls/phylogenetic tree/fastat.fasta", "fasta")

    lens = []

    for record in records:
        print(record.seq)
        ids = record.id
        sequence = record.seq
        lens.append(record.id)
        # print(lens)

    lengthmax = len(max(lens, key=len))
    lengthmin = len(min(lens, key=len))
    line = "  %s             %s\n" % (len(lens), "125")
    file = open("phylo.phy", "w")
    file.write(line)

    for i, id in enumerate(lens):
        if lengthmin < int(lengthmax):
            add = int(lengthmax) - int(len(id))
            # print(i)
            id = id + (add * "-")
            id = id.replace(".", "")
            id = id.replace("_", "")
            to_be_write = "%s%s%s    %s" % (i, "-", id, sequence[0:100])
            # file.write("  %s                    %s\n"%(num_rec,seqlen))
            file.writelines(str("%s\n" % to_be_write))
            print(id)


        else:
            add = int(lengthmax) - int(len(id))
            id = id + (add * "-")
            id = id.replace(".", "")
            id = id.replace("_", "")
            to_be_write = "%s    %s" % (id, sequence[0:100])
            # file.write("  %s                    %s\n"%(num_rec,seqlen))

            file.writelines(str("%s\n" % (to_be_write)))
            print(id)


