import itertools
import math

with open('data/8.txt') as f:
    steps = f.readline().strip()
    next(f)
    tree = {}
    starts = []
    while line:=f.readline().strip():
        node, nexts = line.split(' = ')
        nexts = nexts.strip('()').split(', ')
        tree[node] = nexts
        if node.endswith('A'):
            starts.append(node)

def p1():
    counter = 0
    current = 'AAA'
    for step in itertools.cycle(steps):
        if current == 'ZZZ':
            return counter    
        next = 0 if step == 'L' else 1
        current = tree[current][next]    
        counter += 1

def p2():
    patterns = {}
    for start in starts:        
        counter = 0
        current = start
        ended = []
        for step in itertools.cycle(steps):
            if current in ended:
                break          
            if current.endswith('Z'):
                ended.append(current)
                patterns[start] = counter
            next = 0 if step == 'L' else 1
            current = tree[current][next]    
            counter += 1
    return math.lcm(*patterns.values())


print(p1())
print(p2())
