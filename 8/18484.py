from itertools import product

counter = 1


for value in product(sorted(set("ПАВСИКАКИЙ")), repeat=6):
    value = ''.join(value)

    if 'АА' in value or 'ИИ' in value or 'АИ' in value or 'ИА' in value:
        if value == 'КАКААА':
            print(counter)
            break
        counter += 1



