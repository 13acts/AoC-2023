from itertools import cycle

with open('data/8.txt') as f:
    steps = f.readline().strip()
    next(f)
    tree = {}
    while line := f.readline().strip():
        node, nexts = line.split(' = ')
        nexts = nexts.strip('()').split(', ')
        tree[node] = nexts

counter = 0
current = 'AAA'
for step in cycle(steps):
    if current == 'ZZZ':
        print(counter)
        exit()    
    next = 0 if step == 'L' else 1
    current = tree[current][next]    
    counter += 1
