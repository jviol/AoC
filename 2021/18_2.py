from collections import deque

number1 = "[[[[4,3],4],4],[7,[[8,4],9]]]"
number2 = "[1,1]"

def add_numbers(n1:deque, n2:deque):
    res = n1 + n2
    res.appendleft('[')
    res.append(']')
    return res

number = deque(c for c in (number1+number2) if c != ',')
print(number)

def try_explode(number):
    depth = 0
    for c in enumerate(number):
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        elif 