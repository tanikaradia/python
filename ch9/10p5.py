words=['a','e','i','o','u']

with open('poem3.txt') as f:
    content=f.read()

for word in words:
    # contentNew=content.replace(word,'*'*len(word)) #it only takes last change u
    content=content.replace(word,'*'*len(word))

with open('poem3.txt','w') as f:
    f.write(content)