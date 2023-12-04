with open('data/3.txt') as f:
    lines = f.read().split('\n')

numbers = {}
gears = []

for i, line in enumerate(lines):
    num = ''
    coords = []
    for j, c in enumerate(line):
        # Track num as long as c is digit
        if c.isdigit():
            num += c
            coords += [(i, j)]

            # Number at the end of line
            if j == len(line)-1:
                numbers[tuple(coords)] = int(num)
                num = ''
                coords = []

        # End of consecutive digits
        elif num:
                numbers[tuple(coords)] = int(num)
                num = ''
                coords = []

        # Find gears
        if c == '*':
            gears += [(i, j)]

total = 0
checked = []
for (a, b) in gears:

    surrounds = []
    for i in range(a-1, a+2):
        if i < 0 or i > len(lines)-1:
            continue
        
        for j in range(b-1, b+2):
            if j < 0 or j > len(line)-1:
                continue

            if (i, j) in checked:
                continue

            # Check 8 cells around gear, if there's a number, add to surrounds
            # Then add all coordinates of that number to exclude from next check
            if lines[i][j].isdigit():
                for coords, number in numbers.items():
                    if (i, j) in coords:
                        surrounds += [number]
                        checked += coords

    # Validate
    if len(surrounds) == 2:
        total += surrounds[0] * surrounds[1]

print(total)