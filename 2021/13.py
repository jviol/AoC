
points = set()
folds = []
with open('input/13.txt') as f:
    for line in f:
        if ',' in line:
            x,y = line.split(',')
            points.add((int(x), int(y)))
        elif line.startswith('fold along'):
            axis, value = line[10:16].strip().split('=')
            folds.append((axis, int(value)))

part1 = True
for axis, line in folds:
    if axis == 'x':
        points = {(x,y) if x < line else (2*line-x, y) for x,y in points}
        if part1:
            print('Part 1:', len(points))
            part1 = False
    else:
        points = {(x,y) if y < line else (x, 2*line-y) for x,y in points}

columns = max(x for x,y in points)+1
for y in range(max(y for x,y in points)+1):
    print(''.join('#' if (x,y) in points else ' ' for x in range(columns)))

