with open('input/01.txt') as f:
    depths = [int(line) for line in f]

print('Part 1:', sum(depths[i]<depths[i+1] for i in range(len(depths)-1)))
print('Part 2:', sum(depths[i]<depths[i+3] for i in range(len(depths)-3)))
