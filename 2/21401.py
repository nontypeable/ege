from itertools import permutations, product


def function(x: int, y: int, w: int, z: int):
    return x and (z <= w) and not (y)


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    table = ((x1, x2, 1, x3, 1), (x4, 1, 0, x5, 1), (1, 0, x6, x7, 1))

    if len(table) == len(set(table)):
        for p in permutations("xywz", r=4):
            if all(function(**dict(zip(p, l))) == l[-1] for l in table):
                print(*p)
