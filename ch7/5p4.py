# check prime

n=int(input('no. '))

for i in range(2,n):
    if(n%i==0):
        print('noott primee')
        break
else:
    print('yes prime :)')