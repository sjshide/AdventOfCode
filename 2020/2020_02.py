from utils import *

inp = get_input(2020,2)


# Parse the strings, and run the appropriate counts.

def problem_2():
    ct_1 = 0
    ct_2 = 0
    for x in inp:
        t = x.split(' ')
        let = t[1][0]
        word = t[2]


        minim, maxim = [int(p) for p in t[0].split('-')]

        let_ct = word.count(let)
        if let_ct>=minim and let_ct<=maxim:
            ct_1+=1

        check = 0
        if let==word[minim-1]:
            check+=1
        if let==word[maxim-1]:
            check+=1
        if check==1:
            ct_2+=1
        
        
    return(ct_1,ct_2)


a1, a2 = problem_2()

print('Part A Solution:', a1)
print('Part B Solution:', a2)