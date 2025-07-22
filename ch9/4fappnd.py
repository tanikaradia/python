st='writing new data in a file \n'

# f=open('file2.txt','a')
# f.write(st)

f=open('file2.txt','a+')
f.write(st)
f.seek(0)
print(f.read())

f.close()