from collections import defaultdict
import string

with open('data/7.txt') as f:
    deck = {}
    line = f.readline().strip().split()
    while line:
        deck[line[0]] = int(line[1])
        line = f.readline().strip().split()
        
classes = {a: b for (b, a) in enumerate('AKQJT98765432')}
classes = {a: b for (b, a) in zip(string.ascii_letters,'AKQJT98765432')}
# print(classes)


def reorder(draws):
    # unchanged = {a: True for a in draws}
    order = {draw: '' for draw in draws}
    for i in range(5):
        # if len(set(draw[i] for draw in draws)) == 1:
        # if len(set(draw[i] for draw in draws)) != 1:
        # sort = sorted(draws, key=lambda x: classes[x[i]])
        # sort = sorted(set(draw[i] for draw in draws), key=lambda x:classes[x])
        # print(sort)
        for draw in draws:
            order[draw] += str(classes[draw[i]])
    
    print(order)
    # order = {k: int(v) for (k, v) in order.items()}
    # print({k: v for (k, v) in sorted(order.items(), key=lambda x: x[1])})
    order = [k for (k, v) in sorted(order.items(), key=lambda x: x[1], reverse=True)]

    # order = sorted(draws, key=)

    # return list(order.keys())
    return order


def make_trie(draws):
    trie = {}
    
    new_node = 0
    for draw in draws:
        # draw = '$' + draw
        node = 0
        for symbol in draw:
            
            # if already existed an edge with label symbol
            existed = False
            for edge in trie:
                if edge[0] == node and trie[edge] == symbol:
                    node = edge[1]
                    existed = True
                    break
            
            # if such edge doesn't exist
            if not existed:
                new_node += 1
                trie[(node, new_node)] = symbol
                node = new_node
    
    return trie


def type(draw):
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
        case _:
            return 6

score = defaultdict(list)
for draw in deck:
    score[type(draw)] += [draw]

# print(dict(score))

for type_ in score:
    score[type_] = reorder(score[type_])

final_order = [item for l in [x for x in [score[k] for k in sorted(score, reverse=True)]] for item in l]
# final_order.reverse()

print(score)
print(final_order)
# print(deck)

total = sum(deck[draw] * (final_order.index(draw)+1) for draw in deck)
print(total)