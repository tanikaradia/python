f=open('poem.txt')
find=f.read()

if('chaand' in find):
    print('chaand is present')
else:
    print('khoya khoya chaand')

f.close()