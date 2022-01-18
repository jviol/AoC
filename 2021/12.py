from collections import defaultdict


edges = defaultdict(list)
with open('input/12.txt') as f:
    for line in f:
        k,v = line.strip().split('-')
        edges[k].append(v)
        edges[v].append(k)

def paths(cave : str, visited : set):
    if cave == 'end':
        return 1
    if cave in visited:
        return 0
    return sum(paths(c, (visited | {cave}) if cave.islower() else visited) for c in edges[cave])

print('Part 1:', paths('start', set()))

def paths2(cave : str, visited : set):
    if cave == 'end':
        return 1
    if cave in visited:
        if cave == 'start':
            return 0
        else:
            return sum(paths(c, visited) for c in edges[cave])
    return sum(paths2(c, (visited | {cave}) if cave.islower() else visited) for c in edges[cave])

print('Part 2:', paths2('start', set()))
