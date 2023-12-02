from utils import *

inp = get_input(2023,1)

sumA = 0
sumB = 0

for x in inp:
    
    digsA = [int(t) for t in x if t.isdigit()]
    sumA += (10*digsA[0]+digsA[-1])
    
    # originally tried to do a straight up replace, but got burned by the oneight style test
    x=x.replace('one','one1one')
    x=x.replace('two','two2two')
    x=x.replace('three','three3three')
    x=x.replace('four','four4four')
    x=x.replace('five','five5five')
    x=x.replace('six','six6six')
    x=x.replace('seven','seven7seven')
    x=x.replace('eight','eight8eight')
    x=x.replace('nine','nine9nine')
    
    digsB = [int(t) for t in x if t.isdigit()]
    
    sumB += (10*digsB[0]+digsB[-1])


print('Part A Solution:', sumA)
print('Part B Solution:', sumB)