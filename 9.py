with open('data/9.txt') as f:
	seqs = list(map(str.split, f.readlines()))
	for i in range(len(seqs)):
		seqs[i] = list(map(int, seqs[i]))

def next_line(current):
	return [current[i+1] - current[i] for i in range(len(current)-1)]

def p1():
	total = sum(x[-1] for x in seqs)
	for seq in seqs:
		current = seq
		while any(x!=0 for x in current):
			current = next_line(current)
			total += current[-1]
	print(total)

def p2():
	total = 0
	for seq in seqs:
		firsts = [seq[0]]
		current = seq
		while any(x!=0 for x in current):
			current = next_line(current)
			firsts += [current[0]]
		first = 0
		while firsts:
			first = firsts.pop() - first
		total += first
	print(total)

p1()
p2()
