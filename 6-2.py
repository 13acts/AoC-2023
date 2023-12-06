import itertools

with open('data/6.txt') as f:
    time = int(''.join(f.readline().strip().split(': ')[1].split()))
    dist = int(''.join(f.readline().strip().split(': ')[1].split()))

def travelled(held, time):
    return (time - held) * held

valid = 0
reached = False
for held in itertools.count():
    if travelled(held, time) > dist:
        valid += 1
        reached = True
    elif reached:
        break

print(valid)