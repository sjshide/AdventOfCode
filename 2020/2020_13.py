from utils import *

inp = get_input(2020,13)

t = int(inp[0])
buses = [int(bus) for bus in inp[1].split(',') if bus!='x']

# A
minimum_wait = 100000000
best_bus = -1
for bus in buses:
    if (-t)%bus<minimum_wait:
        minimum_wait=(-t)%bus
        best_bus=bus

        
# B
# had to remind myself how the Chinese Remainder Theorem works
# See https://brilliant.org/wiki/chinese-remainder-theorem/ for instance

# Checked additionally that all buses are prime. 
# This lets us use the inverse trick

ps = []
congs = []
buses2 = inp[1].split(',')
for i in range(len(buses2)):
    if buses2[i]!='x':
        ps.append(int(buses2[i]))
        congs.append((-i)%int(buses2[i]))
        
N=1
for p in ps:
    N*=p

ys = [N//x for x in ps]

yinvs = [pow(ys[i],ps[i]-2,ps[i]) for i in range(len(ps))]

ans = 0
for i in range(len(ps)):
    ans+=(congs[i]*ys[i]*yinvs[i])
ans = ans%N

print('Part A Solution:', minimum_wait*best_bus)
print('Part B Solution:', ans)