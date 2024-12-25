from utils import *

inp = get_input(2024,15)

# just bashing. didn't try to think to hard
# A
ind = inp.index('')
g = grid2dict(inp[:ind])
inst = ''
for x in inp[ind:]:
    inst+=x
for x in g:
    if g[x]=='@':
        robotLoc = x

moves = '<>^v'
ds = [(0,-1),(0,1),(-1,0),(1,0)]
      
ry, rx = robotLoc    
for move in inst:
    dind = moves.index(move)
    dy,dx = ds[dind]
    
    i=1
    while g[(ry+i*dy,rx+i*dx)]=='O':
        i+=1
    
    if g[(ry+i*dy,rx+i*dx)]=='.':
        g[(ry,rx)]='.'
        g[(ry+dy,rx+dx)]='@'
        if i>1:
            g[(ry+i*dy,rx+i*dx)]='O'
        ry,rx = ry+dy,rx+dx 
        
A=0    
for x in g:
    if g[x]=='O':
         A+=(100*x[0]+x[1])

# B
# expand the input width
newInp = []
for x in inp[:ind]:
    t1 = str.replace(x,'#','##')
    t2 = str.replace(t1,'O','[]')
    t3 = str.replace(t2,'.','..')
    t4 = str.replace(t3,'@','@.')
    newInp+=[t4]

g=grid2dict(newInp[:ind])

for x in g:
    if g[x]=='@':
        robotLoc = x        
ry, rx = robotLoc    
    
for move in inst:
    dind = moves.index(move)
    dy,dx = ds[dind]
    
    if g[(ry+dy,rx+dx)]=='#':
        #do nothing
        pass
    elif g[(ry+dy,rx+dx)]=='.':
        #step
        g[(ry,rx)]='.'
        g[(ry+dy,rx+dx)]='@'
        ry,rx=ry+dy,rx+dx
    else:
        # touching a box
        if move in '<>':
            # just do the same thing as before:
            i=1
            while g[(ry+i*dy,rx+i*dx)] in '[]':
                i+=1
            if g[(ry+i*dy,rx+i*dx)]=='.':
                for j in range(i,0,-1):
                    g[(ry+j*dy,rx+j*dx)]=g[(ry+(j-1)*dy,rx+(j-1)*dx)]
                
                g[(ry,rx)]='.'
                ry,rx = ry+dy,rx+dx
        
        else: # gotta think more here...
            boxLayers = []
            thisLayer = set()
            wallFlag = 0
            thisLayer.add((ry+dy,rx+dx))
            for (y,x) in list(thisLayer):
                if g[(y,x)]=='[':
                    thisLayer.add((y,x+1))
                else:
                    thisLayer.add((y,x-1))
            
            boxLayers.append(thisLayer)
            
            while True:
                
                thisLayer = boxLayers[-1]
                nextLayer = set()
                for (y,x) in thisLayer:
                    if g[(y+dy,x+dx)]=='#':
                        wallFlag=1
                        break
                    elif g[(y+dy,x+dx)] in '[]':
                        nextLayer.add((y+dy,x+dx))
                for (y,x) in list(nextLayer):
                    if g[(y,x)]=='[':
                        nextLayer.add((y,x+1))
                    else:
                        nextLayer.add((y,x-1))                    
                
                boxLayers.append(nextLayer)
                
                if len(nextLayer)==0:
                    break
                
            if not wallFlag:
                # move stuff
                revLayers = boxLayers[::-1]
                revLayers = revLayers[1:]
                
                for layer in revLayers:
                    for (y,x) in layer:
                        g[(y+dy,x+dx)]=g[(y,x)]
                        g[(y,x)]='.'
                g[(ry+dy,rx+dx)]='@'
                g[(ry,rx)]='.'
                ry,rx = ry+dy,rx+dx
                
B = 0    
for x in g:
    if g[x]=='[':
         B+=(100*x[0]+x[1])

print('Part A Solution:', A)
print('Part B Solution:', B)