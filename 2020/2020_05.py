from utils import *

inp = get_input(2020,5)


def to_bin(x):
    x=x.replace('F','0')
    x=x.replace('B','1')
    x=x.replace('L','0')
    x=x.replace('R','1')
    return(x)


def cumsum(n):
    return((n**2+n)//2)

inp2 = [int((to_bin(x)),2) for x in inp]

ans1 = max(inp2)
ans2 = cumsum(max(inp2)) - cumsum(min(inp2)-1) - sum(inp2)


print('Part A Solution:', ans1)
print('Part B Solution:', ans2)
