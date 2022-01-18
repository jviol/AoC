
from collections import Counter


insertion_rules = {}
with open('input/14.txt') as f:
    template = f.readline().strip()
    for line in f:
        if line.strip():
            k,v = line.strip().split(' -> ')
            insertion_rules[k] = v

def most_minus_least_common(counter):
    mc = counter.most_common()
    return mc[0][1]-mc[-1][1]

C = Counter(template[i:i+2] for i in range(len(template)-1))
char_counter = Counter(template)
for i in range(40):
    if i == 10:
        print('Part 1:', most_minus_least_common(char_counter))
    C1 = Counter()
    for ac, n in C.items():
        b = insertion_rules[ac]
        a,c = ac
        C1[a+b] += n
        C1[b+c] += n
        char_counter[b] += n
    C = C1

print('Part 2:', most_minus_least_common(char_counter))


