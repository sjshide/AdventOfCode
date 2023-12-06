from utils import *

inp = get_input(2023,5)

# Process input
# Represent ranges as [min,max)
# Idea will be just keep track of how each mapping splits up a given range
seeds = [int(x) for x in inp[0].split()[1:]]
seedsA = [(x,x+1) for x in seeds]
seedsB = []
for i in range(0, len(seeds),2):
    seedsB.append((seeds[i],seeds[i]+seeds[i+1]))

# Create the list of maps for each stage
i=3
storedMaps = []
d = dict()
while i<len(inp):
    if not inp[i]:
        storedMaps.append(d)
        d = dict()
        i+=2
    else:
        [dest, src, ran] = [int(x) for x in inp[i].split()]
        d[(src,src+ran)]=(dest,dest+ran)
        i+=1
        
storedMaps.append(d)


# Handle a collection of ranges for a given map
def processRanges(ranges, d):
    
    newRanges = []
    r = dc(ranges)
    
    # While we have a range that hasn't been checked for intersection against every rule in the map
    # Try and intersect
    while r:
        
        # Get current range to check:
        thisRange = r.pop(0)
        
        # Lets us know we've checked all rules in the map
        noOverlapCheck = 1
        
        # For rule in the map
        for rule in d:
            
            #min of range greater than max of rule 
            if thisRange[0]>=rule[1]:
                continue
            # max of range less than min of rule
            elif thisRange[1]<=rule[0]:
                continue
                
            # otherwise, some overlap:
            else:
                
                aMin,aMax = thisRange
                bMin,bMax = rule
                
                cMin = max(aMin,bMin)
                cMax = min(aMax,bMax)
                
                delta = cMin-bMin
                ruleRange = d[rule]
                newRanges.append((ruleRange[0]+delta,ruleRange[0]+(cMax-cMin)+delta))
                
                # If the range we're checking doesn't fully overlap the rule
                # save the remaining stuff back to r to check against other rules
                if aMin<cMin:
                    r.append((aMin,cMin))
                if cMax<aMax:
                    r.append((cMax,aMax))
                
                noOverlapCheck = 0
                
                break
                
        # if the current range doesn't intersect any rule
        # it just stays itself, so add it to newRanges
        if noOverlapCheck:
            newRanges.append(thisRange)
            
    return(newRanges)


# Handle all maps:
def processAll(l,dList):
    newL = list(l)
    for d in dList:
        newL = processRanges(newL,d)
    return(newL) 



print('Part A Solution:', min([x[0] for x in processAll(seedsA,storedMaps)]))
print('Part B Solution:', min([x[0] for x in processAll(seedsB,storedMaps)]))