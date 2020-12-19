from utils import *

inp = get_input(2020,19)

i = inp.index('')
rules = inp[:i]
msgs = inp[i+1:]


rz = dd(list)
for x in rules:
    key, vals = x.split(': ')
    for y in vals.split(' | '):
        rz[key]+=([t for t in y.split(' ')])

        
rz['35']=['b']
rz['43']=['a']
rz['63'] = ['35', ' ', '43', ' '] # only one with a singles split, hard coding for now.
rz['a'] = ['a']
rz['b'] = ['b']


valid_dd = dd(list)

for t in ['42','31']:
    valid = [[t]]
    for _ in range(20): #idk I don't wanna think about it. full depth was like 11, so this is more than enough
        new_valid = []
        for x in valid:
            this = []
            for y in x:
                if len(rz[y])<4:
                    this+=[tuple([rz[y],rz[y]])]
                else:
                    this.append((rz[y][:2],rz[y][2:]))

            exp = [[]]

            for x in this:
                if x[0]!=x[1]:
                    l1 = [t+x[0] for t in exp]
                    l2 = [t+x[1] for t in exp]
                    exp = l1+l2
                else:
                    exp = [t + x[0] for t in exp]
            new_valid+=exp

        valid=new_valid
    valid_dd[t] = valid



def check(x,part):
    if part=='A':
        if len(x)!=24:
            return(0)
    m = len(x)//8
    l = list(x)
    pcs = []
    for i in range(m):
        pcs.append(l[8*(i):8*(i+1)])
    i = 0
    midi = 0

    while i<m and pcs[i] in valid_dd['42']:
        i+=1

    midi=int(i)
    while i<m and pcs[i] in valid_dd['31']:
        i+=1
    
    if midi>1 and midi < m and i==m and m<2*midi:
        return(1)
    return(0)

ans_A=0
ans_B=0
for x in msgs:
    ans_A+=check(x,'A')
    ans_B+=check(x,'B')

print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)