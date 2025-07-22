t=int(input('no. of rows '))

# print('*'*t)

for i in range(1,t+1):
    if(i==1 or i==t):    #added if elssee
        print('*'*t)
    else:
        print('*'+(' '*(t-2)+'*'))
# else:
#     print('*'*t)
