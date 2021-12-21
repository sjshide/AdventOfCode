from utils import *

inp = get_input(2021,21)

# can probably be sped up significantly.
# pretttyyyy slow

p1, p2 = [int(x.split(' ')[-1]) for x in inp]

# A

die = 0
diect = 0
p1s = 0
p2s = 0

while True:
    turn_rolls = []
    
    for _ in range(6):
        if die==100:
            die=0
        die+=1
        turn_rolls.append(die)
        
    diect+=3
    p1 = (((p1+turn_rolls[0]+turn_rolls[1]+turn_rolls[2]-1)%10)+1)
    p1s+=p1
    if p1s>=1000:
        break
    
    diect+=3
    p2 = (((p2+turn_rolls[3]+turn_rolls[4]+turn_rolls[5]-1)%10)+1)
    p2s+=p2
    if p2s>=1000:
        break
        
A = diect*min(p1s,p2s)

# B

# number of ways to hit a given number with 3 3-sided dice
scores = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}

p1, p2 = [int(x.split(' ')[-1]) for x in inp]

active_games = [(p1,0,p2,0,1)]
# current p1 square, current p1 score, current p2 square, current p2 score, # of games to this point

p1_wins = 0
p2_wins = 0

while active_games:
    new_active_games = []
    
    for game in active_games:
        #p1 goes
        p1 = game[0]
        
        for step1 in range(3,10):
            nexp1 = ((p1+step1-1)%10) + 1
            
            if game[1]+nexp1>=21:
                p1_wins+=game[4]*scores[step1]
                
            else:
                p2 = game[2]
                
                for step2 in range(3,10):
                    nexp2 = ((p2+step2-1)%10)+1
           
                    if game[3]+nexp2>=21:
                        p2_wins+=game[4]*scores[step1]*scores[step2]
                    
                    
                    else:
                        new_active_games.append((nexp1, game[1]+nexp1,
                                                 nexp2, game[3]+nexp2,
                                                 game[4]*scores[step1]*scores[step2]
                                                )
                                               )
    active_games = new_active_games

B = max(p1_wins,p2_wins)


print('Part A Solution:', A)
print('Part B Solution:', B)