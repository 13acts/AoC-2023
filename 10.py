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
        for a in range(self.w):
            for b in range(self.h):
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

count = 0
while next_node.label != S:
    previous = current
    current = next_node
    next_node = Node(next_node.next_node(previous=previous))
    count += 1

print((count//2)+1)