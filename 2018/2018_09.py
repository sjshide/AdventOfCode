from utils import *

inp = get_input(2018,9)

players = int(inp.split(' ')[0])
mm = int(inp.split(' ')[-2])

def score(players, mm):
    cw = dict()
    ccw = dict()
    cw[0]=0
    ccw[0]=0
    
    scores = dict()
    
    curr = 0
    
    for x in range(players):
        scores[x]=0
        
    for i in range(mm):
        mn = i+1
        if mn%23:
            l = cw[curr]
            r = cw[cw[curr]]
            
            cw[l]=mn
            ccw[r]=mn
            cw[mn]=r
            ccw[mn]=l
            
            curr=mn
        else:
            player = i%players
            
            scores[player]+=mn
            
            this = int(curr)
            for _ in range(7):
                this=ccw[this]
            
            scores[player]+=this
            l = ccw[this]
            r = cw[this]
            
            cw[l]=r
            ccw[r]=l
            curr=r
    
    return(max(scores[t] for t in scores))

print('Part A Solution:', score(players, mm))
print('Part B Solution:', score(players,mm*100))