from statistics import mode
from collections import Counter

with open('input/03.txt') as f:
    bins = [line.strip() for line in f]

gamma = ''.join(mode(bin[d] for bin in bins) for d in range(12))
g = int(gamma, 2)
e = g ^ 0xFFF
epsilon = f"{e:b}".zfill(12)
print('Part 1:', e*g)

def most_common(lst):
    cntr = Counter(lst)
    if(cntr['1'] == cntr['0']):
        return '1'
    else:
        return cntr.most_common(1)[0][0]

def least_common(lst):
    cntr = Counter(lst)
    if(cntr['1'] == cntr['0']):
        return '0'
    else:
        return cntr.most_common(2)[1][0]

def get_rating(criteria):
    candidates = bins[:]
    i = 0
    while len(candidates) > 1:
        bit = criteria([b[i] for b in candidates])
        candidates = [b for b in candidates if b[i] == bit]
        i += 1
    return int(candidates[0], 2)

oxy_rating = get_rating(most_common)
co2_rating = get_rating(least_common)

print('Part 2:', oxy_rating*co2_rating)

