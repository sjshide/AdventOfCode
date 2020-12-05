from utils import *

inp = get_input(2020,5)


def to_bin(x):
    x=x.replace('F','0')
    x=x.replace('B','1')
    x=x.replace('L','0')
    x=x.replace('R','1')
    return(x)


def bin_to_id(x):
    row = 0
    col = 0
    
    rev = x[::-1]
    cols = rev[:3]
    rows = rev[3:]
    
    for i in range(3):
        col+=pow(2,i)*int(cols[i])
    for i in range(7):
        row+=pow(2,i)*int(rows[i])

    return(8*(row)+col)


def cumsum(n):
    return((n**2+n)//2)

inp2 = [bin_to_id(to_bin(x)) for x in inp]

ans1 = max(inp2)
ans2 = cumsum(max(inp2)) - cumsum(min(inp2)-1) - sum(inp2)


print('Part A Solution:', ans1)
print('Part B Solution:', ans2)