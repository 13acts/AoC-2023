I = '|'
H = '-'
F = 'F'
J = 'J'
L = 'L'
T = '7'

S = 'S'

class Layout:
    def __init__(self, data) -> None:
        self.data = data
        self.w = len(data[0])
        self.h = len(data)

    def __str__(self) -> str:
        return self.data
    
    def start(self):
        for a in range(self.w):
            for b in range(self.h):
                if data[a][b] == S:
                    return (a,b)        



class Node:
    def __init__(self, coord):
        self.coord = coord
        self.label = layout.data[coord[0]][coord[1]]

    def __str__(self) -> str:
        return f'{self.coord}: {self.label}'

    def next_node(self, previous:'Node'=None):
        i, j = self.coord
        match self.label:
            case '|':
                # if i in (0, layout.h):
                #     return
                return [x for x in [(i+1, j), (i-1, j)] if x != previous.coord][0]
            case '-':
                # if j in (0, layout.w):
                #     return
                return [x for x in [(i, j+1), (i, j-1)] if x != previous.coord][0]
            case 'F':
                # if i == layout.h or j == layout.w:
                #     return
                return [x for x in [(i+1, j), (i, j+1)] if x != previous.coord][0]
            case '7':
                # if i == layout.h or j == 0:
                #     return
                return [x for x in [(i+1, j), (i, j-1)] if x != previous.coord][0]
            case 'J':
                # if i == 0 or j == 0:
                #     return
                return [x for x in [(i-1, j), (i, j-1)] if x != previous.coord][0]
            case 'L':
                # if i == 0 or j == layout.w:
                #     return
                return [x for x in [(i-1, j), (i, j+1)] if x != previous.coord][0]
            case 'S':
                raw_options = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                options = raw_options[:]
                if i == 0:
                    options.remove((i-1, j))
                elif i == layout.h:
                    options.remove((i+1, j))
                if j == 0:
                    options.remove((i, j-1))
                elif j == layout.w:
                    options.remove((i, j+1))
                
                valid = [[I, J, L], [I, F, T], [H, T, J], [H, L, F]]
                for option in options:
                    if layout.data[option[0]][option[1]] in valid[raw_options.index(option)]:
                        return option


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

print(count)
print((count//2)+1)