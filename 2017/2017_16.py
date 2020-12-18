from utils import *

inp = get_input(2017,16)

def apply_move(l, move):
    l=list(l)
    
    if move[0]=='s':
        steps = int(move[1:])
        l = l[-steps:]+l[:-steps]

    if move[0]=='x':
        ind1,ind2 = [int(x) for x in move[1:].split('/')]
        l[ind1],l[ind2]= l[ind2],l[ind1]
        
    if move[0]=='p':
        chars = [x for x in move[1:].split('/')]
        ind1 = l.index(chars[0])
        ind2 = l.index(chars[1])
        l[ind1],l[ind2]= l[ind2],l[ind1]
    
    ans = ''
    for x in l:
        ans+=x
    return(ans)


ans_A = 'abcdefghijklmnop'
for x in (inp.split(',')):
    ans_A = apply_move(ans_A,x)
    

init = 'abcdefghijklmnop'
seen = set()
ct = 0
while True:
    ct+=1
    for x in (inp.split(',')):
        init = apply_move(init,x)
    if init in seen:
        cyc = ct
        break
    else:
        seen.add(init)
        
ans_B = 'abcdefghijklmnop'
for _ in range(1_000_000_000%(cyc-1)):
    for x in (inp.split(',')):
        ans_B = apply_move(ans_B,x)
    


print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)