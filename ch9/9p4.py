#find,replace word in file

word=' a ' #otherwise all a's are replaced

with open('poem2.txt') as f:
    content=f.read()

contentNew=content.replace(word,' the ')

with open('poem2.txt','w') as f:
    f.write(contentNew)