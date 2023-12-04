# 12 red cubes, 13 green cubes, and 14 blue cubes
cap = {"red": 12, "green": 13, "blue": 14}

with open('2.txt') as f:
	lines = f.read().split('\n')

total_id = 0
for i, line in enumerate(lines):
	line = line.split(': ')[1]
	cases = line.split('; ')
	
	line_fail = False
	
	for case in cases:
		cubes = case.split(', ')
		for cube in cubes:
			# print(cube)
			count, color = cube.split()
			if cap[color] < int(count):
				line_fail = True
				break
			
	if not line_fail:
		total_id += i+1
		
print(total_id)