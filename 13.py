from icecream import ic
import random

with open('data/13.txt') as f:
    data = []
    maze = []
    for line in f.read().splitlines() + ['']:
        if line:
            maze += [line]
        else:
            data += [maze]
            maze = []
    # ic(data)


def hori_mirror(maze) -> int:
    '''
    Number of rows above each horizontal line of reflection
    '''
    # ic(maze)
    upper = [maze[0]]
    lower = []
    for line in maze[1:]:        
        if len(lower) == len(upper):
            return len(upper)
        
        if lower:
            if line == upper[-len(lower)-1]:
                lower += [line]
            else:
                upper += lower + [line]
                lower = []
        elif line == upper[-1]:
            lower = [line]
        else:
            upper += [line]
    
    # ic(upper, lower)
    if len(upper) < len(maze):
        return len(upper)
    else:
        return False


def transpose(maze):
    return [''.join(x) for x in zip(*maze)]


ic('index  012345678901234567890')

total = 0
# for maze in data:
# n = random.randint(0, len(data)-1)
n = 15
for maze in data[n:n+1]:
    if k := hori_mirror(maze):
        ic(maze)
        # with open('log_me.txt', 'a') as f:
        #     f.write(f'{k*100}\n')
        total += k*100
    else:
        ic(transpose(maze))
        k = hori_mirror(transpose(maze))
        # with open('log_me.txt', 'a') as f:
        #     f.write(f'{k}\n')
        total += hori_mirror(transpose(maze))
print(total)