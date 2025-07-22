# factorial

n=int(input('a no. '))

def fact(num):
    if(num==0 or num==1):
        return 1
    
    # num=num*fact(num-1)
    return num*fact(num-1)

a=fact(n)
print('factorial is',a)