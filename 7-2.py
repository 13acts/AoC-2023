from collections import defaultdict
import string
from icecream import ic

with open('data/7.txt') as f:
    deck = {}
    line = f.readline().strip().split()
    while line:
        deck[line[0]] = int(line[1])
        line = f.readline().strip().split()
        
hands = dict(zip('AKQT98765432J', string.ascii_letters))


def type(draw:str):
    j = draw.count('J')

    replaced = False
    for c in draw:
        if draw.count(c) == max(draw.count(x) for x in draw) and c != 'J':
            draw = draw.replace('J', c)
            replaced = True
            break
    
    if not replaced:
        draw1 = draw.replace('J', '')
        for c in draw1:
            if draw1.count(c) == max(draw1.count(x) for x in draw1):
                draw = draw.replace('J', c)
                break

    match len(set(draw)):
        case 1:
            return 0
        case 2:
            if draw.count(draw[0]) in (1, 4):
                return 1
            else:
                return 2
        case 3:
            x = 1 if draw.count(draw[0]) == 1 else 0
            if draw.count(draw[x]) in (1, 3):
                return 3
            elif draw.count(draw[x]) == 2:
                return 4
        case 4:
            return 5
        case 5:
            return 6


def reorder(draws):
    recode = {draw: '' for draw in draws}
    for i in range(5):
        for draw in draws:
            recode[draw] += hands[draw[i]]    
    return [kv[0] for kv in sorted(recode.items(), key=lambda x:x[1], reverse=True)]


# Classify deck into types
types = defaultdict(list)
for draw in deck:
    types[type(draw)] += [draw]

# For each type, reorder from low to high score
for type_ in types:
    types[type_] = reorder(types[type_])

# Flatten types into list
order = [item for l in [x for x in [types[k] for k in sorted(types, reverse=True)]] for item in l]

ic(types)
print(order)

# Calculate sum
print(sum(deck[draw] * (order.index(draw)+1) for draw in deck))

# print(reorder(['JKKK2', 'QQQQ2']))
print(type('J25T4'))