from utils import *

# Represent as digraphs to keep track of lying on / lying below relations

inp = get_input(2023,22)

# Parse bricks, putting z first so we can sort by z value
bricks = dict()
rev = dict()
for i in range(len(inp)):
    b = inp[i]
    b = b.replace('~',',')
    x1,y1,z1,x2,y2,z2 = tuple([int(t) for t in b.split(',')])
    # put z first for sorting?
    bricks[i] = (min(z1,z2),max(z1,z2),min(x1,x2),max(x1,x2),min(y1,y2),max(y1,y2))
    rev[(min(z1,z2),max(z1,z2),min(x1,x2),max(x1,x2),min(y1,y2),max(y1,y2))] = i

# drop the bricks from lowest z to highest z    
fallen = dict()
for b in sorted(bricks.values()):
    bNum = rev[b]
    cubes = []
    for z in range(b[0],b[1]+1):
        for x in range(b[2],b[3]+1):
            for y in range(b[4],b[5]+1):
                cubes.append([z,x,y])
    i=0
    while not len([(c[0]-i,c[1],c[2]) for c in cubes if (((c[0]-i,c[1],c[2]) in fallen) or (c[0]-i<=0))]):
        i+=1
    i-=1
    for c in cubes:
        fallen[(c[0]-i,c[1],c[2])]=bNum

GUp = nx.DiGraph()
GDown = nx.DiGraph()
for i in bricks:
    GUp.add_node(i)
    GDown.add_node(i)    
for (z,x,y) in fallen:
    if (z-1,x,y) in fallen and fallen[(z,x,y)]!=fallen[(z-1,x,y)]:
        GUp.add_edge(fallen[(z-1,x,y)],fallen[(z,x,y)])
        GDown.add_edge(fallen[(z,x,y)],fallen[(z-1,x,y)])        

# A: find bricks which are not the sole brick supporting another brick
necCheck = dict()
for i in bricks:
    necCheck[i]=1
for i in bricks:
    nbs = list(GDown.neighbors(i))
    if len(nbs)==1:
        necCheck[nbs[0]]=0
A = sum(necCheck.values())

# B: For each brick, find all bricks that fall if each brick is removed
# Need to check that a given brick lies only on bricks that fall
# So need both up and down relations
# Didn't really require top sort, but why not       
srtUp = list(nx.topological_sort(GUp))
B = 0
for x in srtUp:
    onTop = set([x])
    nbs = list(GUp.neighbors(x))
    while nbs:
        n = nbs.pop(0)
        locNbs = list(GDown.neighbors(n))
        if not len([t for t in locNbs if t not in onTop]):
            onTop.add(n)
            nbs = nbs+list(GUp.neighbors(n))
    B+=(len(onTop)-1)
        
print('Part A Solution:', A)
print('Part B Solution:', B)