from utils import *

inp = get_input(2023,6)

times = inp[0].split()[1:]
dists = inp[1].split()[1:]

timesA = [int(x) for x in times]
distsA = [int(x) for x in dists]

timesB = int(''.join(times))
distsB = int(''.join(dists))

#(x*(time-x))>dist
# -x^2 + (time)x - dist > 0
# (-time +/- sqrt((time^2 - 4dist))/-2)
def getWinningCt(time, dist):
    root1 = (time - math.sqrt(time*time - 4*dist))/2
    root2 = (time + math.sqrt(time*time - 4*dist))/2
    
    return(math.floor(root2)-math.floor(root1))

print('Part A Solution:', math.prod([getWinningCt(timesA[i],distsA[i]) for i in range(len(times))]))
print('Part B Solution:', getWinningCt(timesB,distsB))