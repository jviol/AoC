import re
from itertools import combinations
import numpy as np

scanners = []
with open('input/19.txt') as f:
    scanner_pattern = re.compile('--- scanner (\d+) ---')
    for line in f:
        line = line.strip()
        if line:
            if scanner_pattern.match(line):
                scanner = []
                scanners.append(scanner)
            else:
                scanner.append(np.fromiter(map(int, line.split(',')), np.short))

relative_positions = []
for scanner in scanners:
    relative_positions.append({tuple(sorted(map(abs, b0-b1))):(tuple(b0),tuple(b1)) for b0,b1 in combinations(scanner, 2)})
    assert len(relative_positions[-1]) == len(scanner)*(len(scanner)-1)//2

def find_common_beacon(bp0, bp1):
    return set(bp0) & set(bp1)



count = 0
for i,j in combinations(range(25), 2):
    rp0:dict = relative_positions[i]
    rp1:dict = relative_positions[j]
    overlap = rp0.keys() & rp1.keys()
    overlapping_values = ((rp0[k], rp1[k]) for k in overlap)
    for a,b in combinations(overlapping_values, 2):
        s0bp0, s1bp0 = a
        s0bp1, s1bp1 = b
        cbi = find_common_beacon(s0bp0, s0bp1)
        cbj = find_common_beacon(s1bp0, s1bp1)
        if cbi:
            assert cbj

        count += 1
        #print(a,b,c,d,x)
    for i, k1 in combinations(overlap, 2):
        pass
print(count)
exit()



    # overlapping0 = {k:rp0[k] for k in overlap}
    # overlapping1 = {k:rp1[k] for k in overlap}
    # print('Overlap of scanner', i, 'and', j)
    #    print('\t', relpos0[k], relpos1[k])

            

for i, l in enumerate(scanners):
    print('Scanner', i)
    for beacon in l:
        print(beacon)
