in_path = "/home/peter/Desktop/dividing_lines.txt"
out_path = "/home/peter/Desktop/out_path.txt"




list = []
list2 = []
file = open(in_path,'r')
reads = file.readlines()

for line in reads:
    print(line)
    list.append(line)
print(list)




readlen = 59
start = 0
end = 1
endprocc = 0
while endprocc < readlen:
    for str in list:
        list2.append(str[start:end])
    start = start+20
    end = end + 20
    endprocc = endprocc + 20


                                                                         #print(str[0:19])
                                                                        # list2.insert(0,str[0:19])
                                                                     # list2.insert(1,str[19:39])
                                                                       # list2.insert(2,str[39:59])

print(list2)
