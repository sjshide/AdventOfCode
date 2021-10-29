from utils import *

inp = get_input(2018,5)

#A
s = str(inp)
while True:
    new = ''
    i=0
    while i+1 < len(s):
        this=s[i]
        if this.islower():
            if this.upper()==s[i+1]:
                i+=2
            else:
                new+=this
                i+=1
        elif this.isupper():
            if this.lower()==s[i+1]:
                i+=2
            else:
                new+=this
                i+=1
    if i==len(s)-1:
        new+=s[i]
    if new==s:
        break
    else:
        s=new
A = len(s)


#B. pretty slow but don't wanna think more about it
best_len=pow(10,10)
for rem in 'abcdefghijklmnopqrstuvwxyz':
    s = str(inp)
    while True:
        new = ''
        i=0
        while i+1 <len(s):
            this=s[i]
            if this==rem or this==rem.upper():
                i+=1
            elif this.islower():
                if this.upper()==s[i+1]:
                    i+=2
                else:
                    new+=this
                    i+=1
            elif this.isupper():
                if this.lower()==s[i+1]:
                    i+=2
                else:
                    new+=this
                    i+=1
        if i==len(s)-1 and s[i] not in [rem,rem.upper()]:
            new+=s[i]
        if new==s:
            break
        else:
            s=new
    if len(s)<best_len:
        best_len=len(s)
B = best_len



print('Part A Solution:', A)
print('Part B Solution:', B)