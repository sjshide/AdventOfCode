from utils import *

inp = get_input(2017,3)

def xy_pt(n):
    i=0
    while (2*i+1)**2<n:
        i+=1
    x,y = i,-i
    top = (2*i+1)**2
    step = (2*i+1)
    dif = top-n
    
    x-=min(dif,2*i)
    dif-=min(dif,2*i)
    if dif>0:
        y+=min(dif,2*i)
        dif-=min(dif,2*i)
    if dif>0:
        x+=min(dif,2*i)
        dif-=min(dif,2*i)
    if dif>0:
        y-=min(dif,2*i)
        dif-=min(dif,2*i)
    
    
    return(abs(x)+abs(y))



### OEIS
url = 'https://oeis.org/A141481/b141481.txt'
response = requests.get(url=url).text

for x in response.split('\n')[2:]:
    if int(x.split(' ')[1])>int(inp):
        ans_B = int(x.split(' ')[1])
        break


print('Part A Solution:', xy_pt(int(inp)))
print('Part B Solution:', ans_B)