from utils import *

inp = get_input(2021,2)

# An impressive 2 wrong submissions on A. Reading errors.

hor, ver_A, ver_B, aim = 0, 0, 0, 0

for x in inp:
    direc, n = x.split(' ')
    num = int(n)
    
    if direc == 'forward':
        hor+=num
        ver_B+=(aim*num)
    if direc == 'down':
        ver_A+=num
        aim+=num
    if direc == 'up':
        ver_A-=num
        aim-=num


print('Part A Solution:', hor*ver_A)
print('Part B Solution:', hor*ver_B)