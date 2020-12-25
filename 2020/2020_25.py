from utils import *

inp = [int(x) for x in get_input(2020,25)]

mod = 20201227

def get_loop(public_key):
    start = 1
    subj = 7
    ct = 0
    while True:
        ct+=1
        start = (start*subj)%mod
        if start==public_key:
            return(ct)
        
def get_key(loop,public):
    start = 1
    subj = public
    for _ in range(loop):
         start=(start*subj)%mod    
    return(start)

loops = [get_loop(x) for x in inp]
key1, key2 = [get_key(loops[i],inp[1-i]) for i in range(2)]
if key1==key2:
    ans_A=key1
else:
    ans_A = 'SOMETHING WRONG!'
    
print('Part A Solution:', ans_A)
print('Part B Solution:', 'Click the link!')