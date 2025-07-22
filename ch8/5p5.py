n=int(input('n: '))

##normal fun
# def patt(p):
#     print(p*'*')

# for i in range(n,0,-1):
#     patt(i)

def patt(p):
    if(p==0): return

    print(p*'*')
    patt(p-1)

patt(n)