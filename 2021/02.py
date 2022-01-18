from collections import defaultdict

with open('input/02.txt') as f:
    dirs = defaultdict(lambda:0)
    aim = 0
    depth = 0
    for line in f:
        d, l = line.split()
        l = int(l)
        dirs[d] += l
        match d:
            case 'down':    aim+=l
            case 'up':      aim-=l
            case 'forward': depth+=aim*l

print('Part 1:', dirs['forward']*(dirs['down']-dirs['up']))
print('Part 2:', dirs['forward']*depth)