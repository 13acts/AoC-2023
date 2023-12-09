with open('data/9.txt') as f:
	alls = list(map(str.split, f.readlines()))
	for i in range(len(alls)):
		alls[i] = list(map(int, alls[i]))

def p1():
	total = sum(x[-1] for x in alls)
	for seq in alls:
		current = seq
		while any(x!=0 for x in current):
			tmp_current = []
			for i in range(len(current)-1):
				tmp_current += [current[i+1] - current[i]]
			current = tmp_current.copy()
			total += current[-1]
	print(total)

def p2():
	total = 0
	for seq in alls:
		firsts = [seq[0]]
		current = seq
		while any(x!=0 for x in current):
			tmp_current = []
			for i in range(len(current)-1):
				tmp_current += [current[i+1] - current[i]]
			current = tmp_current.copy()
			firsts += [current[0]]
		tmp = 0
		while firsts:
			tmp = firsts.pop() - tmp
		total += tmp
	print(total)

p1()
p2()