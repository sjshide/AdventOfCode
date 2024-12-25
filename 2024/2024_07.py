from utils import *
from functools import lru_cache

inp = get_input(2024,7)

@lru_cache
def check(val, nums, part):
    if val<0:
        return(0)
    if len(nums)==1:
        if val==nums[0]:
            return(1)
        else:
            return(0)
    else:
        l = list(nums)
        last = l.pop(-1)
        
        modCheck = ((val%last)==0)
        s1 = str(val)
        s2 = str(last)
        concatCheck = s1[-len(s2):]==s2
        
        if modCheck:
            a=check(val//last,tuple(l),part)
        else:
            a=0
    
        if concatCheck and len(s1[:-len(s2)])>0:
            b = check(int(s1[:-len(s2)]),tuple(l),part)
        else:
            b=0
            
        if part=='A':
            return max(check(val-last,tuple(l),part),a)
        elif part=='B':
            return max(check(val-last,tuple(l),part),a,b)

A = 0
B = 0
for x in inp:
    val,nums = x.split(': ')
    val = int(val)
    nums = tuple([int(t) for t in nums.split()])
    
    if check(val, nums, 'A'):
        A+=val
    if check(val, nums, 'B'):
        B+=val
        
print('Part A Solution:', A)
print('Part B Solution:', B)