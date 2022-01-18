
from collections import defaultdict


inputs = []
outputs = []

with open('input/08.txt') as f:
    for line in f:
        input, output = line.strip().split('|')
        inputs.append(input.strip().split())
        outputs.append(output.strip().split())

print('Part 1:', sum(len(x) in [2,4,3,7] for output in outputs for x in output))

def as_string(S):
    return ''.join(sorted(S))

total = 0
for input, output in zip(inputs, outputs):
    combined = input + output
    count_dict = defaultdict(list)
    for p in combined:
        count_dict[len(p)].append(set(p))
    one = count_dict[2][0]
    four = count_dict[4][0]
    seven = count_dict[3][0]
    eight = count_dict[7][0]
    three = None
    for p in count_dict[5]:
        if not one - p:
            three = p
            break
    mid = three & four - one
    top_left = four - three
    nine = three | top_left
    zero = eight - mid
    five = None
    two = None
    for p in count_dict[5]:
        if p != three:
            if top_left & p:
                five = p
            else:
                two = p
    top_right = one & two
    six = eight - top_right
    values = dict(zip(map(as_string, [zero, one, two, three, four, five, six, seven, eight, nine]), range(10)))
    for i,s in enumerate(output):
        total += values[as_string(s)] * 10**(3-i)

print('Part 2:', total)

    