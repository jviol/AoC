from itertools import chain
from math import inf

matrix = []
with open('input/11.txt') as f:
    for line in f:
        matrix.append([int(c) for c in line.strip()])

flashes = 0
ly = len(matrix)
lx = len(matrix[0])
step = 0
while True:
    step += 1
    for row in matrix:
        for i in range(lx):
            row[i] += 1

    flash = True
    while(flash):
        flash = False
        for y in range(ly):
            for x in range(lx):
                if matrix[y][x] > 9:
                    matrix[y][x] = -inf
                    flash = True
                    flashes += 1
                    for x0 in [x-1,x,x+1]:
                        for y0 in [y-1,y,y+1]:
                            if (not x0-x == 0 == y0-y 
                                    and 0 <= x0 < lx
                                    and 0 <= y0 < ly):
                                matrix[y0][x0] += 1
    for y in range(ly):
        for x in range(lx):
            if matrix[y][x] < 0:
                matrix[y][x] = 0
    if all(x == 0 for row in matrix for x in row):
        print('Part 2: step', step)
        break
    if step == 100:
        print('Part 1:', flashes) 