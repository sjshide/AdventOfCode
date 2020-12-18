from utils import *

inp = get_input(2017,11)

def grid_steps(s):
    l = s.split(',')
    x,y = 0,0
    loc_max = 0
    norm = complex(1/2,math.sqrt(3)/2)
    base = 0
    
    for inst in l:
        if inst=='n':
            base+=norm**0
        elif inst=='nw':
            base+=norm**1
        elif inst=='sw':
            base+=norm**2
        elif inst=='s':
            base+=norm**3
        elif inst == 'se':
            base+=norm**4
        if inst == 'ne':
            base+=norm**5
    
        y = 2*base.imag/math.sqrt(3)
        x = (abs(2*base.real) - abs(y))/2 
        loc_max = max(loc_max,abs(x)+abs(y))
    
    return(abs(x)+abs(y), loc_max)

ans_A, ans_B = grid_steps(inp)

print('Part A Solution:', round(ans_A))
print('Part B Solution:', round(ans_B))