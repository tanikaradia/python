#tables

def table(n):
    with open(f'tables/table{n}.txt','w') as f: #make folder earlier
        for i in range(1,11):
            f.write(f'{n}*{i}={n*i}\n')

for i in range(2,21):
    table(i)