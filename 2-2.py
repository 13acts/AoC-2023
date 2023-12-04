from collections import defaultdict

with open('2.txt') as f:
	lines = f.read().split('\n')

total = 0
for i, line in enumerate(lines):
	line = line.split(': ')[1]
	cases = line.split('; ')
	
	min_count = defaultdict(int)
	for case in cases:
		cubes = case.split(', ')
		for cube in cubes:
			count, color = cube.split()
			min_count[color] = max(min_count[color], int(count))
			
	prod = 1
	for x in min_count.values():
		prod *= x
	total += prod
		
print(total)