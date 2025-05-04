from itertools import permutations, product


def function(x: int, y: int, w: int, z: int):
    return (x and not (y)) or (y == z) or w


for x1, x2, x3, x4 in product([0, 1], repeat=4):
    table = (
        (x1, x2, 1, x3, 0),
        (0, 0, 0, 1, 0),
        (1, 0, x4, 1, 0),
    )

    if len(table) == len(set(table)):
        for p in permutations("xywz", r=4):
            if all(function(**dict(zip(p, l))) == l[-1] for l in table):
                print(*p)
