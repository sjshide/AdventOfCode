from utils import *

inp = get_input(2020,12)

dirs = {'N': 0+1j, 'S': 0-1j, 'E':1, 'W': -1}
turns = {'L':1, 'R':-1}

def manh_dist(comp):
    return(abs(comp.real)+abs(comp.imag))

def process_A(instr_list):
    pos = 0+0j
    direc = 1
    
    for instruction in instr_list:
        inst = instruction[0]
        n = int(instruction[1:])
        if inst in dirs:
            pos+=n*dirs[inst]
        if inst in turns:
            this_turn = n//90
            direc*=pow(0+1j,turns[inst]*this_turn)
        if inst =='F':
            pos+=n*direc
                
    return(int(manh_dist(pos)))


def process_B(instr_list):
    ship_pos = 0+0j
    wp_pos = 10+1j

    for instruction in instr_list:
        inst = instruction[0]
        n = int(instruction[1:])
        if inst in dirs:
            wp_pos+=n*dirs[inst]
        if inst in turns:
            this_turn = n//90
            wp_pos*=pow(0+1j,turns[inst]*this_turn)
        if inst =='F':
            ship_pos+=n*(wp_pos)

    return(int(manh_dist(ship_pos)))


print('Part A Solution:',process_A(inp))
print('Part B Solution:',process_B(inp))