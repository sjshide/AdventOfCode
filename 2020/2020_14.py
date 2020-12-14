from utils import *
from collections import defaultdict as dd


inp = get_input(2020,14)

# Part A
mem_A = dd(int)
for x in inp:
    if x[:4]=='mask':
        mask = x.split('= ')[1]
    else:
        loc = int(x.split(']')[0][4:])
        val = int(x.split('= ')[1])
        bin_val = '0'*(36-len(bin(val)[2:]))+bin(val)[2:]
        
        ans = ''
        for i in range(36):
            if mask[i]!='X':
                ans+=mask[i]
            else:
                ans+=bin_val[i]
        
        mem_A[loc]=int(ans,2)
    

    
# Part B
# At most 9 X's in all of my masks, so fine to just brute force.

mem_B = dd(int)
for x in inp:
    if x[:4]=='mask':
        mask = x.split('= ')[1]
    else:
        loc = int(x.split(']')[0][4:])
        val = int(x.split('= ')[1])
        
        bin_loc = '0'*(36-len(bin(loc)[2:]))+bin(loc)[2:]

        ans = ['']
        for i in range(36):
            loc_ans = []
            if mask[i]=='X':
                for y in ans:
                    loc_ans.append(y+'0')
                    loc_ans.append(y+'1')
            elif mask[i]=='0':
                for y in ans:
                    loc_ans.append(y+bin_loc[i])
            elif mask[i]=='1':
                for y in ans:
                    loc_ans.append(y+'1')
            ans=loc_ans
        for key in ans:
            mem_B[int(key,2)]=val

            
            
ans_A = 0
ans_B = 0
for key in mem_A:
    ans_A+=mem_A[key]
for key in mem_B:
    ans_B+=mem_B[key]
            
print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)