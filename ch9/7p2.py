import random

def game():
    print('The game starts: ')
    score=random.randint(1,51)

    with open('hiscore.txt') as f:
        hi=f.read()
        if(hi==''): hi=0
        else: hi=int(hi) #as read gives str

    print(f'The previous high score was {hi}\nAnd current score is {score}')

    if(score>hi):
        with open('hiscore.txt','w') as f:
            f.write(str(score))
            print(f'Your new high score becomes {score}')
    else: print('No change')

    return score

game()