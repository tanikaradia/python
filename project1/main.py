# rock -1
# paper 0
# scissors 1
import random

bot=random.choice([-1,0,1])

uStr=input('Choose for rock(r), paper(p), scissors(s): ')
if uStr not in ['r', 'p', 's']:
    print("Invalid input! Please try again.")
    exit()

uDict={'r':-1,'p':0,'s':1}
revDict={-1:'rock',0:'paper',1:'scissors'}

user=uDict[uStr]

print(f'You chose {revDict[user]} & Computer chose {revDict[bot]}')

if(user==bot):
    print('Draw!')

else:
    if(user==1 and bot==0 ):  #u-b=1
        print('You win!')
    elif(user==1 and bot==-1):  #u-b=2
        print('Computer win!')

    elif(user==0 and bot==-1):  #u-b=1
        print('You win!')
    elif(user==0 and bot==1 ):  #u-b=-1
        print('Computer win!')
        
    elif(user==-1 and bot==1 ):  #u-b=-2
        print('You win!')
    elif(user==-1 and bot==0 ):  #u-b=-1
        print('Computer win!')

    else:
        print('something is fishy...')

# a logic can be made that if(u-b==1 or -2): then user always WIN