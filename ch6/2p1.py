# greatest of 4

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))

if(a>=b and a>=c and a>=d):
    print('a')
elif(b>=a and b>=c and b>=d): # elif(b>a and b>c and b>d): nooo
    print('b')
elif(c>=b and c>=a and c>=d):
    print('c')
elif(d>=b and d>=c and d>=a):
    print('d')
