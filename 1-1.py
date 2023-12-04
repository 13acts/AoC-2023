with open('data/1.txt') as f:
    lines = f.readlines()
	
sum = 0
for line in lines:
	for c in line:
		if c.isdigit():
			break            
	for d in line[::-1]:
		if d.isdigit():
			break
	sum += int(c+d)
    
print(sum)