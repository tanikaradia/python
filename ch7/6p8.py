t=int(input('no. of rows '))

for i in range(1,t+1):
    # for j in range(1,i+1):
    print('*'*i)

# orr

for i in range(1, t+1):
    for j in range(1, i+1):
        print('*', end='')  # ✅ print * without newline
    print()  # newline after each row
