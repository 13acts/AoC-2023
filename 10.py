I = '|'
H = '-'
F = 'F'
T = '7'
J = 'J'
L = 'L'
S = 'S'

class Layout:
    def __init__(self, data) -> None:
        self.data = data
        self.w = len(data[0])
        self.h = len(data)

    def __str__(self) -> str:
        return self.data
    
    def start(self) -> tuple:
        for a in range(self.h):
            for b in range(self.w):
                if data[a][b] == S:
                    return (a,b)        


class Node:
    def __init__(self, coord) -> None:
        self.coord = coord
        self.label = layout.data[coord[0]][coord[1]]

    def __str__(self) -> str:
        return f'{self.coord}: {self.label}'

    def next_node(self, previous:'Node'=None) -> tuple:
        i, j = self.coord
        match self.label:
            case '|':
                return [x for x in [(i+1, j), (i-1, j)] if x != previous.coord][0]
            case '-':
                return [x for x in [(i, j+1), (i, j-1)] if x != previous.coord][0]
            case 'F':
                return [x for x in [(i+1, j), (i, j+1)] if x != previous.coord][0]
            case '7':
                return [x for x in [(i+1, j), (i, j-1)] if x != previous.coord][0]
            case 'J':
                return [x for x in [(i-1, j), (i, j-1)] if x != previous.coord][0]
            case 'L':
                return [x for x in [(i-1, j), (i, j+1)] if x != previous.coord][0]
            case 'S':
                options = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                if i == 0:
                    options.remove((i-1, j))
                elif i == layout.h:
                    options.remove((i+1, j))
                if j == 0:
                    options.remove((i, j-1))
                elif j == layout.w:
                    options.remove((i, j+1))                
                valid = {(i+1, j): [I, J, L],
                         (i-1, j): [I, F, T],
                         (i, j+1): [H, T, J],
                         (i, j-1): [H, L, F]}
                for coord in options:
                    if layout.data[coord[0]][coord[1]] in valid[coord]:
                        return coord


with open('data/10.txt') as f:
    data = f.read().splitlines()
    layout = Layout(data)


def valid_i(i):
    '''Check if i in-range'''
    return -1 < i < layout.h
def valid_j(j):
    '''Check if j in-range'''
    return -1 < j < layout.w


def adj(coord:tuple, k:int=None):
    '''
    Find adjacent coordinates, if in range
    Optional k: index of adjacent node to grab coordinate, if left empty, return all adjacent coordinates
    '''
    i, j = coord
    options = [(i-1,j-1), (i-1,j), (i-1,j+1),
               (i, j-1), (i, j), (i,j+1),
               (i+1,j-1), (i+1,j), (i+1,j+1)]
    if k is not None:
        if valid_i(options[k][0]) and valid_j(options[k][1]):
            return options[k]
        else:
            return None
    else:
        return set(options)


def sides_outlines() -> tuple[set]:
    '''
    Follow along path and separate adjacent coordinates of path into left side and right sight
    '''
    "Corner case: Starting node is not accounted when searching for adj nodes"    
    ref = {I: ([3], 5, 7),
           H: ([1], 7, 3),
           F: ((0,1,3), 8, 7),
           T: ((1,2,5), 6, 3),
           J: ((5,7,8), 0, 1),
           L: ((3,6,7), 2, 5)}
    
    previous = path.pop()
    side_L = set()
    side_R = set()
    while path:
        node = path.pop()
        if node.label == S:
            continue
        coord = node.coord
        a, b, c = ref[node.label]

        side_1 = {adj(coord, x) for x in a}
        side_2 = {adj(coord, b)}
        left, right = (side_1, side_2) if previous.coord == adj(coord, c) else (side_2, side_1)
        side_L = side_L.union(left)
        side_R = side_R.union(right)

        previous = node
    side_L.discard(None)
    side_R.discard(None)
    return side_L-path_coords, side_R-path_coords


def inner() -> tuple:
    '''
    Identify inner outline
    '''
    a, b = sides_outlines()
    for coord in a:
        if coord[0] == 0 or coord[1] == 0:
            return b
    return a


def spiral_expand(coord) -> set:
    '''
    From coordinate, spiral outwards to find all coordinates in batch
    '''
    a, b = coord
    result = {coord}
    d = 1
    looping = True
    while looping:
        looping = False
        for i in range(a-d, a+d+1):
            if not valid_i(i):
                continue
            for j in range(b-d, b+d+1):
                if not valid_j(j) or i not in (a-d, a+d+1):
                    continue
                if (i, j) not in path_coords and (i, j) not in result and result.intersection({adj((i, j), k) for k in (1,3,5,7)}):
                    result.add((i, j))
                    looping = True
        d += 1
    return result




############## PART 1 ######################
current = Node(layout.start())
next_node = Node(current.next_node())

path = [current, next_node]
path_coords = {current.coord, next_node.coord}
while next_node.label != S:
    previous = path[-2]
    current = path[-1]
    next_node = Node(next_node.next_node(previous=previous))
    
    path += [next_node]
    path_coords.add(next_node.coord)

print(len(path)//2)
############################################


############## PART 2 ######################
# Removes last cycling node
path.pop()
all_inner = set()
for coord in inner():
    if coord in all_inner:
        continue
    all_inner = all_inner.union(spiral_expand(coord))

print(len(all_inner))
############################################
