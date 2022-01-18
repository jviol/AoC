from functools import reduce
import operator

heightmap = []
with open('input/09.txt') as f:
    for line in f:
        heightmap.append([int(c) for c in line.strip()])

def explore_basin(y, x, basin):
    if heightmap[y][x] == 9 or (y,x) in basin:
        return basin
    else:
        basin.add((y,x))
        if y > 0:
            basin = explore_basin(y-1, x, basin)
        if y < len(heightmap)-1:
            basin = explore_basin(y+1, x, basin)
        if x > 0:
            basin = explore_basin(y, x-1, basin)
        if x < len(heightmap)-1:
            basin = explore_basin(y, x+1, basin)
        return basin

basins = []
risk_level = 0
for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        h = heightmap[y][x]
        if y > 0 and heightmap[y-1][x] <= h:
            continue
        if y < len(heightmap) - 1 and heightmap[y+1][x] <= h:
            continue
        if x > 0 and heightmap[y][x-1] <= h:
            continue
        if x < len(heightmap[0]) - 1 and heightmap[y][x+1] <= h:
            continue
        risk_level += 1 + h
        basins.append(explore_basin(y, x, set()))
        
print('Part 1:', risk_level)
print('Part 2:', reduce(operator.mul, sorted(len(b) for b in basins)[-3:]))