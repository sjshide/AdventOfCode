from utils import *
from collections import defaultdict as dd

inp = get_input(2020,6)

def pt_A():
    ct = 0
    seen_yes = set()
    for x in inp:
        if x == '':
            ct+=len(seen_yes)
            seen_yes=set()
        else:
            for question in x:
                seen_yes.add(question)
    ct+=(len(seen_yes))
    return(ct)


def pt_B():
    ct = 0
    seen_yes = dd(int)
    pers_ct = 0
    for x in inp:
        if x == '':
            for t in seen_yes:
                if seen_yes[t]==pers_ct:
                    ct+=1
            seen_yes=dd(int)
            pers_ct=0
        else:
            pers_ct+=1
            for m in x:
                seen_yes[m]+=1
    for t in seen_yes:
        if seen_yes[t]==pers_ct:
            ct+=1
    return(ct)

print('Part A Solution:', pt_A())
print('Part B Solution:', pt_B())