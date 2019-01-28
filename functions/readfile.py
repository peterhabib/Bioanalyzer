file = open("/home/peter/Desktop/Moduls/test_data/test.txt" , 'r')
x =file.read()
list = []
print(list)
list.append(x)
codon = "ATG"
print(list)
print(x.count(codon))
print(x.replace("\n" , "").count(codon))



