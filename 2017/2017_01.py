from utils import *

inp = get_input(2017,1)


def rol_dig_sum(n):
    tot_A = []
    tot_B = []
    
    str_A = n+n[0]
    str_B = n*2
    
    for i in range(len(n)-1):
        if str_A[i]==str_A[i+1]:
            tot_A.append(int(str_A[i]))
    
    step = len(n)//2
    for i in range(len(n)-1):
        if str_B[i]==str_B[i+step]:
            tot_B.append(int(str_B[i]))
    return(sum(tot_A),sum(tot_B))


A,B = rol_dig_sum(inp)

print('Part A Solution:',A)
print('Part B Solution:',B)