import sys
sys.setrecursionlimit(100000)

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
    data = list(map(str.strip, f.readlines()))
    layout = Layout(data)

current = Node(layout.start())
next_node = Node(current.next_node())

path = [current, next_node]
while next_node.label != S:
    previous = path[-2]
    current = path[-1]
    next_node = Node(next_node.next_node(previous=previous))

    path += [next_node] # next_node need itself to update, so can't integrate



print(len(path)//2) # path currentlys has S at start and end
path.pop()
# print(path[-1])

def valid_i(i):
    return -1 < i < layout.h
def valid_j(j):
    return -1 < j < layout.w

def adj(coord:tuple, k:int=None):
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

path_coords = {node.coord for node in path}

def sides_outlines():
    # print(path_coords)

    previous = path.pop()
    print(previous)
    side_L = set()
    side_R = set()
    while path:
        print(previous)
        node = path.pop()
        label = node.label
        coord = node.coord
        print(coord)
        match label:
            case '|':
                side_1 = {adj(coord, 3)}
                side_2 = {adj(coord, 5)}
                if previous.coord == adj(coord, 7):
                    side_L = side_L.union(side_1)
                    side_R = side_R.union(side_2)
                else:
                    side_L = side_L.union(side_2)
                    side_R = side_R.union(side_1)
            case '-':
                side_1 = {adj(coord, 1)}
                side_2 = {adj(coord, 7)}
                if previous.coord == adj(coord, 3):
                    side_L = side_L.union(side_1)
                    side_R = side_R.union(side_2)
                else:
                    side_L = side_L.union(side_2)
                    side_R = side_R.union(side_1)
            case 'F':
                side_1 = {adj(coord, x) for x in (0, 1, 3)}
                side_2 = {adj(coord, 8)}
                if previous.coord == adj(coord, 7):
                    side_L = side_L.union(side_1)
                    side_R = side_R.union(side_2)
                else:
                    side_L = side_L.union(side_2)
                    side_R = side_R.union(side_1)
            case '7':
                side_1 = {adj(coord, x) for x in (1, 2, 5)}
                side_2 = {adj(coord, 6)}
                if previous.coord == adj(coord, 3):
                    side_L = side_L.union(side_1)
                    side_R = side_R.union(side_2)
                else:
                    side_L = side_L.union(side_2)
                    side_R = side_R.union(side_1)
            case 'J':
                side_1 = {adj(coord, x) for x in (5, 7, 8)}
                side_2 = {adj(coord, 0)}
                if previous.coord == adj(coord, 1):
                    side_L = side_L.union(side_1)
                    side_R = side_R.union(side_2)
                else:
                    side_L = side_L.union(side_2)
                    side_R = side_R.union(side_1)
            case 'L':
                side_1 = {adj(coord, x) for x in (3, 6, 7)}
                side_2 = {adj(coord, 2)}
                if previous.coord == adj(coord, 5):
                    side_L = side_L.union(side_1)
                    side_R = side_R.union(side_2)
                else:
                    side_L = side_L.union(side_2)
                    side_R = side_R.union(side_1)

        previous = node
    side_L.discard(None)
    side_R.discard(None)
    # print(side_L)
    # print(side_R)
    return side_L-path_coords, side_R-path_coords

def inner_outer() -> tuple:
    a, b = sides_outlines()
    for coord in a:
        if coord[0] == 0 or coord[1] == 0:
            return b, a
    return a, b

def expand(coord) -> set:
    def expand_LU(coord, result:set):
        if coord in path_coords:
            return set()    
        result.add(coord)
        for next in [adj(coord, x) for x in (1,3)]:
            result = result.union(expand_LU(next, result))    
        return result
    def expand_UR(coord, result:set):
        if coord in path_coords:
            return set()    
        result.add(coord)
        for next in [adj(coord, x) for x in (1,5)]:
            result = result.union(expand_UR(next, result))
        return result
    def expand_RD(coord, result:set):
        if coord in path_coords:
            return set()    
        result.add(coord) 
        for next in [adj(coord, x) for x in (5,7)]:
            result = result.union(expand_RD(next, result))
        return result
    def expand_DL(coord, result:set):
        if coord in path_coords:
            return set()    
        result.add(coord)  
        for next in [adj(coord, x) for x in (3,7)]:
            result = result.union(expand_DL(next, result))
        return result
    result = expand_LU(coord, set())
    print(result)
    result = result.union(expand_UR(coord, set()))
    print(result)
    result = result.union(expand_RD(coord, set()))
    print(result)
    result = result.union(expand_DL(coord, set()))
    print(result)
    return result

def spiral_expand(coord) -> set:
    a, b = coord
    result = {coord}
    search_range = 1
    looping = True
    while looping:
        looping = False
        for i in range(a-search_range, a+search_range+1):
            if not valid_i(i):
                continue
            for j in range(b-search_range, b+search_range+1):
                if not valid_j(j):
                    continue
                if (i, j) not in path_coords and (i, j) not in result and result.intersection({adj((i, j), k) for k in (1,3,5,7)}):
                    result.add((i, j))
                    looping = True
        search_range += 1
    return result


# print(adj((102, 116), 0))
# print(adj((102, 116), 1))
# print(adj((102, 116), 3))
# print(set(adj((102, 116), x) for x in (0, 1, 3)))

inner, outer = inner_outer()
print(len(inner))
# print(inner)

# print(spiral_expand((81, 76)))
# print(spiral_expand((5, 11)))

all_inner = set()
for coord in inner:
    print(coord)
    all_inner = all_inner.union(spiral_expand(coord))

# print(all_inner)
print(len(all_inner))

