# is comment spam??

a='buy now'
b='click on link'
c='subscribe now'
d='reading for free'
# e=['bhai','link','gaali','free'] #opp syntax
# lekin fir jo comment me likhe vo exact hona chahiye e se

comment=input('comment here: ')

if((a in comment) or (b in comment) or (c in comment) or (d in comment)): #loook e  (comment in e)
    print('SPAMM!')
else:
    print('ok')
