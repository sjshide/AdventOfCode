from utils import *

# frustrating night. turns out my choice of key for checking repeats was 
# very bad. amazing that a few extra brackets could've saved 3 hrs
# took forever to figure out what was wrong...

inp = get_input(2020,22)

split = inp.index('')

p1 = [int(x) for x in inp[1:split]]
p2 = [int(x) for x in inp[split+2:]]


def score(deck):
    total = 0
    for i in range(len(deck)):
        total+=deck[::-1][i]*(i+1)
    return total

def game(P1,P2):
    X,Y = P1.copy(),P2.copy()
    while X and Y:
        x = X.pop(0)
        y = Y.pop(0)
        if x>y:
            X+=[x,y]
        else:
            Y+=[y,x]
    if X:
        return(X)
    else:
        return(Y)

part_B_winner = []
def rec_game(P1,P2):
    global part_B_winner
    X,Y = P1.copy(),P2.copy()
    this_mem = set()
    winner = 0
    while X and Y:
        if tuple(X+[0]+Y) in this_mem: #this killed me. was originally tuple(X+Y).
            winner=1
            break
        else:
            this_mem.add(tuple(X+[0]+Y))
            
            x = X.pop(0)
            y = Y.pop(0)
            
            if (x<=len(X)) and (y<=len(Y)):
                rd_winner = rec_game(X[:x],Y[:y])
            else:
                if x>y:
                    rd_winner=1
                elif y>x:
                    rd_winner=2
            if rd_winner == 1:
                X=X+[x,y]
            elif rd_winner == 2:
                Y=Y+[y,x]
                
    if not winner:
        if X:
            winner=1
            part_B_winner = X
        elif Y:
            winner=2
            part_B_winner = Y
    return(winner)

ans_A = score(game(p1,p2))

rec_game(p1,p2)
ans_B = score(part_B_winner)

print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)