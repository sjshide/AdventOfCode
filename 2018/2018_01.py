from utils import *

inp = get_input(2018,1)
int_inp = [int(x) for x in inp]


#A
A = sum(int_inp)


#B
seen = set()
current = 0

check=0

while True:
    for x in int_inp:
        current+=x
        if current in seen:
            B=current
            check=1
            break
        else:
            seen.add(current)
    if check:
        break



print('Part A Solution:', A)
print('Part B Solution:', B)