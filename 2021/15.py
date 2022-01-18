from collections import defaultdict
from math import inf
from datetime import datetime
from queue import PriorityQueue



with open(r'C:\Users\u4007607\Documents\code\AoC\input\15.txt') as f:
    risk_levels = [[int(x) for x in line.strip()] for line in f]

for row in risk_levels:
    lx = len(row)
    for i in range(lx, 5*lx):
        row.append(row[i-lx] % 9 + 1)

ly = len(risk_levels)
for j in range(ly, 5*ly):
    row = risk_levels[j-ly]
    risk_levels.append([x % 9 + 1 for x in row])

ly = len(risk_levels)
lx = len(risk_levels[0])

class BitSet():
    def __init__(self) -> None:
        self.long = int('0'*ly*lx, 2)

def neighbours(v):
    x,y = v
    return ((x0,y0) for x0,y0 in [(x,y-1), (x,y+1), (x-1,y), (x+1, y)] if 0 <= x0 < lx and 0 <= y0 < ly)

Q = PriorityQueue()

total_risk = defaultdict(lambda:inf)
total_risk[(0,0)] = 0
visited = set()
current = (0,0)
i = 0
j = 0
start = datetime.now()
to_visit = set()
while True:
    visited.add(current)
    for u in neighbours(current):
        if u not in visited:
            x,y = u
            if u not in to_visit:
                total_risk[u] = min(total_risk[current] + risk_levels[y][x], total_risk[u])
                Q.put((total_risk[u], u))
                to_visit.add(u)
    if Q.empty():
        break
    _, current = Q.get_nowait()
    to_visit.remove(current)
    #i += 100
    #if i >= lx*ly:
    #    j += 1
    #    i = 0
    #    #print('['+'='*j+' '*(99-j)+']', str(j+1)+'%', datetime.now()-start, end='\r')
print(datetime.now()-start)


# for y in range(ly):
#     print([total_risk[(x,y)] for x in range(lx)])
print('Part 2:', total_risk[(lx-1, ly-1)])


