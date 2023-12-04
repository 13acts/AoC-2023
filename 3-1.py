with open('data/3.txt') as f:
    lines = f.read().split('\n')

numbers = {}

for i, line in enumerate(lines):
    num = ''
    coords = []
    for j, c in enumerate(line):
        if c.isdigit():
            num += c
            coords += [(i, j)]

            if j == len(line)-1:
                numbers[tuple(coords)] = int(num)
                num = ''
                coords = []

        elif num:
                numbers[tuple(coords)] = int(num)
                num = ''
                coords = []

total = 0
for coords, number in numbers.items():
    found = False
    for (a, b) in coords:        
        if found:
            continue

        for i in range(a-1, a+2):
            if i < 0 or i > len(lines)-1:
                continue
            
            for j in range(b-1, b+2):
                if j < 0 or j > len(line)-1:
                    continue

                if not lines[i][j].isdigit() and lines[i][j] != '.':
                    total += number
                    found = True
                    break

print(total)