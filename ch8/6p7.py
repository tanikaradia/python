# remove specific set of letters ONLY from start/end =strip
l=['tani','rani','shaani','ravi','chandani']

def s(l,letters):
    n=[]
    for i in l:
        n.append(i.strip(letters))
    return n
    
print(s(l,'ni'))