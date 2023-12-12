N = 1000000
#N = 2
E = '.'
O = '#'

with open('data/11.txt') as f:
	layout = f.read().splitlines()

did = False
hori = []
vert = []
galaxies = []
for i in range(len(layout)):
	# empty line
	if all(x==E for x in layout[i]):
		hori.append(i)
	
	for j in range(len(layout[0])):
		# empty column
		if not did and all(x[j]==E for x in layout):
			vert.append(j)
			
		# is galaxy
		if layout[i][j] == O:
			galaxies.append((i, j))
	did = True

cache = {}
def extra(t, ref):
	if t in cache:
		return cache[t]
	else:
		cache[t] = cache[(t[1], t[0])] = (N-1) * len([x for x in ref if min(t)<=x<=max(t)])
		return cache[t]

total = 0
for i, a in enumerate(galaxies):
	for b in galaxies[:i]:
		total += abs(a[0]-b[0])+extra((a[0], b[0]), hori) + abs(a[1]-b[1])+extra((a[1], b[1]), vert)
	
print(total)