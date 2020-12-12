from utils import *

inp = get_input(2020,12)

def process_A(instr_list):
    pos = 0+0j
    direc = 1
    
    for instruction in instr_list:
        inst = instruction[0]
        n = int(instruction[1:])
        if inst =='N':
            pos+=n*(0+1j)
        if inst =='S':
            pos+=n*(0-1j)
        if inst =='E':
            pos+=n*(1)
        if inst =='W':
            pos+=n*(-1)
        if inst =='F':
            pos+=n*direc
        else:
            this_turn = n//90
            if inst=='L':
                direc*=(pow(0+1j,this_turn))
            if inst=='R':
                direc*=(pow(0+1j,4-this_turn))
    return(int(abs(pos.real)+abs(pos.imag)))


def process_B(instr_list):
    ship_pos = 0+0j
    wp_pos = 10+1j

    for instruction in instr_list:
        inst = instruction[0]
        n = int(instruction[1:])
        if inst =='N':
            wp_pos+=n*(0+1j)
        if inst =='S':
            wp_pos+=n*(0-1j)
        if inst =='E':
            wp_pos+=n*(1)
        if inst =='W':
            wp_pos+=n*(-1)
        if inst =='F':
            ship_pos+=n*(wp_pos)
        else:
            this_turn = n//90
            if inst=='L':
                wp_pos= (wp_pos)*(pow(0+1j,this_turn))
            if inst=='R':
                wp_pos=(wp_pos)*(pow(0+1j,4-this_turn))

    return(int(abs(ship_pos.real)+abs(ship_pos.imag)))

print('Part A Solution:',process_A(inp))
print('Part B Solution:',process_B(inp))