from itertools import permutations
from copy import deepcopy

class Pair:
    def __init__(self, lst) -> None:
        l,r = lst
        self.left = l if isinstance(l, (int, Pair)) else Pair(l)
        self.right = r if isinstance(r, (int, Pair)) else Pair(r)

    def reduce(self):
        while self.try_explode() or self.try_split():
            #print(self)
            pass

    def try_split(self) -> bool:
        if isinstance(self.left, Pair):
            if self.left.try_split():
                return True
        elif self.left >= 10:
            value = self.left
            self.left = Pair((value//2, (value+1)//2))
            return True
        if isinstance(self.right, Pair):
            return self.right.try_split()
        elif self.right >= 10:
            value = self.right
            self.right = Pair((value//2, (value+1)//2))
            return True
        else:
            return False

    def try_explode(self, depth=1):
        if depth == 4:
            if isinstance(self.left, Pair):
                res = (self.left.left, None)
                if isinstance(self.right, Pair):
                    self.right.left += self.left.right
                else:
                    self.right += self.left.right
                self.left = 0
                return res                
            elif isinstance(self.right, Pair):
                res = (None, self.right.right)
                self.left += self.right.left
                self.right = 0
                return res
            else:
                return None
        else:
            res = None
            if isinstance(self.left, Pair):
                res = self.left.try_explode(depth+1)
                if res is True:
                    return res
                if res:
                    l,r = res
                    if l is not None:
                        return res
                    if r is not None:
                        if isinstance(self.right, int):
                            self.right += r
                        else:
                            child = self.right
                            while isinstance(child.left, Pair):
                                child = child.left
                            child.left += r
                        return True  
            if not res and isinstance(self.right, Pair):
                res = self.right.try_explode(depth+1)
                if res is True:
                    return res
                if res:
                    l,r = res
                    if r is not None:
                        return res
                    if l is not None:
                        if isinstance(self.left, int):
                            self.left += l
                        else:
                            child = self.left
                            while isinstance(child.right, Pair):
                                child = child.right
                            child.right += l
                        return True
            if not res:
                return None

    def __add__(self, other):
        p = Pair((deepcopy(self), deepcopy(other)))
        p.reduce()
        return p
    
    def __repr__(self) -> str:
        return f"[{self.left}, {self.right}]"

def magnitude(n):
    if isinstance(n, int):
        return n
    else:
        return 3*magnitude(n.left) + 2*magnitude(n.right)

with open('input/18.txt') as f:
    numbers = [Pair(eval(line.strip())) for line in f]

print('Part 1:', magnitude(sum(numbers[1:], numbers[0])))
print('Part 2:', max(magnitude(n1 + n2) for n1, n2 in permutations(numbers, 2)))
    


