#give line no, word is present
word='shant'

with open('poem.txt') as f:
    lines=f.readlines() #goes line by LINE

lineno=1
for line in lines:
    if(word in line):
        print(f'{word} is present in line {lineno}')
        break
    lineno+=1
else:
    print('word not there')
