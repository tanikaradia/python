f=open('file.txt')

# # lines=f.readlines() #all lines in list form
# # print(lines,type(lines))

# l1=f.readline() #1
# print(l1,type(l1))

# l4=f.readline() #reads line by line seqwise 2
# print(l4)

line=f.readline()
while(line!=''):
    print(line)
    line=f.readline() #needed ->move to next line

f.close()