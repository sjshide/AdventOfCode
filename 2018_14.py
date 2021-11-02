from utils import *

inp = int(get_input(2018,14))

#A
ind1 = 0
ind2 = 1
recs = [3,7]

steps = inp
while len(recs)<inp+15:
    rec_sum = recs[ind1]+recs[ind2]
    for num in str(rec_sum):
        recs.append(int(num))
    ind1 = (1+ind1+recs[ind1])%len(recs)
    ind2 = (1+ind2+recs[ind2])%len(recs)
       
A = ''
for x in recs[steps:steps+10]:
    A+=str(x)


    
    
#B
# start a few steps in so slicing works
# hella if statements about twice as fast as my version without this garbage
# uses the fact that input str length is 6
ind1 = 3
ind2 = 4
recs = [3,7,1,0,1,0]

steps = str(inp)
l = len(steps)
while True:
    rec_sum = recs[ind1]+recs[ind2]
    for num in str(rec_sum):
        recs.append(int(num))
    ind1 = (1+ind1+recs[ind1])%len(recs)
    ind2 = (1+ind2+recs[ind2])%len(recs)
    
    if str(recs[-l]) == steps[0]:
        if str(recs[-l+1])==steps[1]:
            if str(recs[-l+2])==steps[2]:
                if str(recs[-l+3])==steps[3]:
                    if str(recs[-l+4])==steps[4]:
                        if str(recs[-l+5])==steps[5]:
                            B = len(recs)-l
                            break
    if str(recs[-l-1]) == steps[0]:
        if str(recs[-l])==steps[1]:
            if str(recs[-l+1])==steps[2]:
                if str(recs[-l+2])==steps[3]:
                    if str(recs[-l+3])==steps[4]:
                        if str(recs[-l+4])==steps[5]:
                            B = len(recs)-l-1
                            break



print('Part A Solution:',A)
print('Part B Solution:',B)