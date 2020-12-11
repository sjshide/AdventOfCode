from utils import *

from collections import defaultdict as dd

inp = get_input(2020,11)

initial_state = dd(str)

ht = len(inp)
wd = len(inp[0])
for i in range(ht):
    for j in range(wd):
        initial_state[(i,j)]=inp[i][j]

def to_hash(t):
    return (tuple([t[(i,j)] for i in range(ht) for j in range(wd)]))

def viz_ct_check_1(m,y,x):
    total=0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (i,j)!=(0,0):
                if m[(y+i,x+j)]=='#':
                    total+=1
                    
    return(total)   

def update_1(m):
    local = dd(str)
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if m[(i,j)]=='L':
                if not viz_ct_check_1(m,i,j):
                    local[(i,j)] = '#'
            elif m[(i,j)]=='#':
                if viz_ct_check_1(m,i,j)>=4:
                    local[(i,j)]= 'L'
            if not local[(i,j)]:
                local[(i,j)]=m[(i,j)]           
    return(local)  

def part_A(state):   
    s = state.copy()
    seen = set()
    while True:
        this = to_hash(s)
        if this in seen:
            return(this.count('#'))
        
        seen.add(this)
        s = update_1(s)

        
        
def viz_ct_check_2(m,y,x):
    total=0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            I,J =y,x
            if (i,j)!=(0,0):
                while True:
                    I+=i
                    J+=j
                    if m[(I,J)] in ['','L']:
                        break
                    if m[(I,J)]=='#':
                        total+=1
                        break
                    
    return(total)   


def update2(m):
    local = dd(str)
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if m[(i,j)]=='L':
                if not viz_ct_check_2(m,i,j):
                    local[(i,j)] = '#'
            elif m[(i,j)]=='#':
                if viz_ct_check_2(m,i,j)>4:
                    local[(i,j)]= 'L'
            if not local[(i,j)]:
                local[(i,j)]=m[(i,j)]
            
    return(local) 


def part_B(state):
    s = state.copy()
    seen =set()
    ct=0
    while True:
        ct+=1
        this = to_hash(s)
        if this in seen:
            return(this.count('#'))
        seen.add(this)
        s = update2(s)


print('Part A Solution:', part_A(initial_state))
print('Part B Solution:', part_B(initial_state))