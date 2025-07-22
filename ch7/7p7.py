t=int(input('no. of rows '))

for i in range(1,t+1):
    # print(' '*(t-i),'*'*(2*i-1)) #not align
    # print(' '*(t-i)+'*'*(2*i-1))

    print(' '*(t-i),end='')
    print('*'*(2*i-1))
