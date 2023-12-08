import itertools
import math

with open('data/8.txt') as f:
    steps = f.readline().strip()
    next(f)
    tree = {}
    starts = []
    line = f.readline().strip()
    while line:
        node, nexts = line.split(' = ')
        nexts = nexts.strip('()').split(', ')
        tree[node] = nexts
        if node.endswith('A'):
            starts.append(node)
        line = f.readline().strip()

patterns = {}
for start in starts:        
    counter = 0
    current = start
    ended = []
    for step in itertools.cycle(steps):
        if current.endswith('Z'):
            if current in ended:
                break            
            ended.append(current)
            patterns[start] = counter
        next = 0 if step == 'L' else 1
        current = tree[current][next]    
        counter += 1

print(math.lcm(*patterns.values()))