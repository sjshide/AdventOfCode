from utils import *

inp = get_input(2017,2)

cols = [[int(i) for i in x.split('\t')] for x in inp]

ans_A = 0
for x in cols:
    ans_A+=(max(x)-min(x))
    
ans_B =0
for x in cols:
    for i in x:
        for j in x:
            if i!=j and i%j==0:
                ans_B+=(i//j)


print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)