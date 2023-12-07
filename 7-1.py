from collections import defaultdict
import string

with open('data/7.txt') as f:
    deck = {}
    line = f.readline().strip().split()
    while line:
        deck[line[0]] = int(line[1])
        line = f.readline().strip().split()
        
hands = dict(zip('AKQJT98765432', string.ascii_letters))


def type(draw:list):
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

# Calculate sum
print(sum(deck[draw] * (order.index(draw)+1) for draw in deck))
