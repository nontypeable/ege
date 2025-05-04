from itertools import product, permutations


def function(a: int, b: int, c: int, d: int):
    return ((not a) and (not b)) or (b == c) or d


for x1, x2, x3, x4 in product([0, 1], repeat=4):
    table = ((x1, x2, 1, x3, 0), (1, 0, x4, 1, 0), (0, 0, 1, 1, 0))

    if len(table) == len(set(table)):
        for p in permutations("abcd", r=4):
            if all(function(**dict(zip(p, l))) == l[-1] for l in table):
                print(*p)
