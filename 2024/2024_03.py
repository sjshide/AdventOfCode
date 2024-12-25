from utils import *
import re

inp = get_input(2024,3)
temp = str(inp)
# I am garbanzo at regex sure this isn't the cleanest way
x = re.findall('mul\([0-9]+,[0-9]+\)|don\'t|do',temp)

A = 0
B = 0
on = 1
for t in x:
    if t=='do':
        on=1
    elif t=="don't":
        on=0
    else:
        nums = t[4:-1]
        m1,m2 = [int(p) for p in nums.split(',')]
        A+=m1*m2
        B+=on*m1*m2

print('Part A Solution:', A)
print('Part B Solution:', B)