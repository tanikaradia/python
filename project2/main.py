from random import randint
num=randint(0,100)

print('Guess the no. game!\nLets\'s Start:')
user=int(input('Choose a no. '))
guess=1

while (user!=num):
    if(user<0 or user>99):
        print('Enter a valid no. ')
        # exit()

    elif(user>num):
        print('Lower the no. ')
        guess+=1
    elif(user<num):
        print('Increase the no. ')
        guess+=1

    user=int(input('Choose a no. '))


print(f'Yayy! You guessed the right ans in {guess} guess')