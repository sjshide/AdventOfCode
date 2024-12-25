from utils import *
from collections import Counter

inp = get_input(2024,1)

first = []
second = []
for x in inp:
    a,b = x.split()
    first+=[int(a)]
    second+=[int(b)]
    
first = sorted(first)
second = sorted(second)

A = 0
B = 0
C = Counter(second)
for i in range(len(first)):
    A+=abs(first[i]-second[i])
    B+=first[i]*C[first[i]]
    
print('Part A Solution:', A)
print('Part B Solution:', B)