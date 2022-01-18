from statistics import median

matching_brackets = dict(zip('([{<', ')]}>'))
score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
total1 = 0
scores = []
with open('input/10.txt') as f:
    for line in f:
        stack = []
        for c in line.strip():
            if c in '([{<':
                stack.append(c)
            elif matching_brackets[stack.pop()] != c:
                total1 += score[c]
                break # corrupt
        else: # not corrupt
            score2 = 0
            while stack:
                score2 = score2*5 + '.([{<'.index(stack.pop())
            scores.append(score2)

print('Part 1:', total1)
print('Part 2:', median(scores))
