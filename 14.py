from icecream import ic
from collections import defaultdict


with open('data/14.txt') as f:
    layout = f.read().splitlines()


def transpose(maze):
    return [''.join(x) for x in zip(*maze)]

layout = transpose(layout)

# ic(layout)

def solve_line(line):
    n = len(line)
    note = defaultdict(int)
    weight = 0
    i_patch = None
    o_count = 0
    for i, c in enumerate('#'+line+'#'):
        if c == '#':
            if i_patch is None:
                i_patch = i
            else:
                note[i_patch] = o_count
                weight += sum(x for x in range(n-i_patch, n-i_patch-o_count, -1))
                i_patch = i
                o_count = 0
        elif c == 'O':
                o_count += 1
    # return dict(note)
    return weight



ic(solve_line(layout[2]))

print(sum(solve_line(x) for x in layout))