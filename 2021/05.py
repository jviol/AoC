from collections import defaultdict

vectors = []
with open('input/05.txt') as f:
    for line in f:
        split_line = line.strip().split(' -> ')
        vectors.append([tuple(map(int, p.split(','))) for p in split_line])

map = defaultdict(lambda:0)
for v in vectors:
    v0,v1 = v
    if v0[0] == v1[0]:
        x = v0[0]
        start,stop = sorted([v0[1], v1[1]])
        for y in range(start, stop+1):
            map[x,y] += 1
    
    elif v0[1] == v1[1]:
        y = v0[1]
        start,stop = sorted([v0[0], v1[0]])
        for x in range(start, stop+1):
            map[x,y] += 1

    else:
        assert abs(v0[0]-v1[0]) == abs(v0[1]-v1[1])
        x,y = v0
        for i in range(abs(v0[0]-v1[0])+1):
            map[x,y] += 1
            x += 1 if v0[0] < v1[0] else -1
            y += 1 if v0[1] < v1[1] else -1

print(sum(value >= 2 for value in map.values()))
