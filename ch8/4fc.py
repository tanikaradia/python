def f2c(f):
    c=(f-32)*5/9
    return c

f=int(input('in f '))

n=f2c(f)
print(f'{round(n,2)} in c')
# round off till 2 digits

