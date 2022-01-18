from statistics import mean

with open('input/07.txt') as f:
    crab_positions = [int(c) for c in f.read().strip().split(',')]

def triangular(x):
    return x * (x+1) // 2

def test_midpoint(midpoint):
    return sum(triangular(abs(c-midpoint)) for c in crab_positions)

a = int(mean(crab_positions))
va = test_midpoint(a)
vb = test_midpoint(a+1)
if va < vb:
    d = -1
    last = va
    a -= 1
else:
    d = 1
    last = vb
    a += 2

while(True):
    this = test_midpoint(a)
    if last < this:
        print(last)
        exit()
    else:
        last = this
        a += d
