import itertools

with open('data/8.txt') as f:
    steps = f.readline().strip()
    next(f)
    tree = {}
    line = f.readline().strip()
    while line:
        node, nexts = line.split(' = ')
        nexts = nexts.strip('()').split(', ')
        tree[node] = nexts
        line = f.readline().strip()

counter = 0
current = 'AAA'
for step in itertools.cycle(steps):
    if current == 'ZZZ':
        print(counter)
        exit()    
    next = 0 if step == 'L' else 1
    current = tree[current][next]    
    counter += 1
