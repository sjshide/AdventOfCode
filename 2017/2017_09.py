from utils import *

inp = get_input(2017,9)


def rem_exc(s):
    m = len(s)
    new_s = ''
    i = 0
    while i<m:
        check = 0
        this = s[i]
        if this=='!':
            i+=1
            check=1
        if check==0:
            new_s+=this
        i+=1
    return(new_s)

def rem_garb(s):
    new_s = str(s)
    total_rem = 0
    while True:
        try:
            ind = new_s.index('<')
            ind2 = new_s.index('>')
            new_s = new_s[:ind]+new_s[ind2+1:]
            total_rem+=(ind2-ind-1)
        except:
            break
    return(new_s,total_rem)

def score(s):
    depth = 1
    total = 0
    for char in s:
        if char == '{':
            total+=depth
            depth+=1
        elif char =='}':
            depth-=1
    return(total)

clean_inp, ans_B = rem_garb(rem_exc(inp))

print('Part A Solution:', score(clean_inp))
print('Part B Solution:', ans_B)