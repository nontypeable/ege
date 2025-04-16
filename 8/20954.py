from itertools import product

counter = 0

for value in product(sorted("МАКС"), repeat=6):
    counter += 1
    value = "".join(value)
    if 'С' not in value and 'М' not in value and 'КК' not in value:
        print(counter)

