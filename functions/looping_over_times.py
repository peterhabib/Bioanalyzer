sequences=['ATTAGACCTG','CCTGCCGGAA','AGACCTGCCG','GCCGGAATAC']
halfway= len(sequences[0])/2
genome=sequences[0]     # this is the string that will be added onto throughout the loop
sequences.remove(sequences[0])


for j in range(len(sequences)):
    for sequence in sequences:
        front=[]
        back=[]
        for i in range(int(halfway),len(sequence)):

            if genome.endswith(sequence[:i]):
                genome=genome+sequence[i:]
                sequences.remove(sequence)

            elif genome.startswith(sequence[-i:]):
                genome=sequence[:i]+genome
                sequences.remove(sequence)
'''
            elif not genome.startswith(sequence[-i:]) or not genome.endswith(sequence[:i]):

                sequences.remove(sequence)      # this doesnt seem to work want to get rid of 
                                                #sequences that are in the middle of the string and 
                                                 #already accounted for 
'''
print(sequence)