from utils import *

inp = get_input(2017,4)

ct_A = 0
ct_B = 0
for x in inp:
    l1 = len([sorted(t) for t in x.split(' ')])
    l2 = len(set([tuple(sorted(t)) for t in x.split(' ')]))
    
    if len(set(x.split(' ')))==len(x.split(' ')):
        ct_A+=1
        
    if l1==l2:
        ct_B+=1


print('Part A Solution:', ct_A)
print('Part B Solution:', ct_B)