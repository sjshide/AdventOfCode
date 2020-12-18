from utils import *

inp = get_input(2020,18)

# Man I really struggled with this one. First recursive-ish thing I tried seemed to do stuff in the wrong order.
# So discarded and tried "find deepest set of parens, evaluate that, and work outward"
# after many index +/-1 errors, finally got it working.
# Kind of a disaster. The people that just overloaded operators and used eval are geniuses.

# evaluate expressions with no parentheses

def no_pars_A(expr):
    x = expr.split(' ')
    fin = int(x[0])
    next_op=''
    for t in x[1:]:
        if t in '+*':
            next_op=t
        else:
            if next_op=='+':
                fin = fin+int(t)
            elif next_op == '*':
                fin = fin*int(t)
    return(fin)

def no_pars_B(expr):
    x = expr.split(' ')
    while '+' in x:
        ind = x.index('+')
        x = x[:max(0,ind-1)]+[str(int(x[ind-1])+int(x[ind+1]))]+x[min(len(x),ind+2):]
    fin = 1
    for t in x[::2]:
        fin*=int(t)
    return(fin)

# Get array whose ith entry is nonzero if entry is a parenthesis,
# with value = how many paren expressions deep I am,
# and 0 otherwise.

def paren_arr(expr):
    x = str(expr)
    pars = []
    open_ct = 0
    
    for i in range(len(x)):
        if x[i]=='(':
            open_ct+=1
            pars.append(open_ct)
        elif x[i]==')':
            pars.append(open_ct)
            open_ct-=1
        else:
            pars.append(0)
    return(pars)

# find deepest set of parentheses, evaluate the expression in there
# and replace it in the larger expression.
# go til everything's evaluated

def full_eval(expr, eval_fc):
    x = str(expr)
    pars = paren_arr(x)
            
    while sum(pars):
        m = max(pars)
        ind1 = pars.index(m)
        ind2 = pars[ind1+1:].index(m) + ind1 + 1

        x = x[:ind1]+str(eval_fc(x[ind1+1:ind2]))+x[min(ind2+1,len(x)):]
        
        pars = paren_arr(x)
        
    return(eval_fc(x)) 


ans_A = 0
ans_B = 0

for x in inp:
    ans_A+=full_eval(x,no_pars_A)
    ans_B+=full_eval(x,no_pars_B)

print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)