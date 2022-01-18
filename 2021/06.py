from collections import Counter, defaultdict

with open('input/06.txt') as f:
    fish = Counter(map(int, f.read().strip().split(',')))
for day in range(256):
    next_day = defaultdict(lambda:0)
    for clk, n in fish.items():
        if clk == 0:
            next_day[8] = n
            next_day[6] += n
        else:
            next_day[clk-1] += n
    fish = next_day
print(sum(fish.values()))