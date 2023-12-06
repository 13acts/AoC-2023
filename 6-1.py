import itertools

with open('data/6.txt') as f:
    times = list(map(int, f.readline().strip().split(': ')[1].split()))
    dists = list(map(int, f.readline().strip().split(': ')[1].split()))

def travelled(held, time):
    return (time - held) * held

ans = 1
for i, time in enumerate(times):
    dist = dists[i]
    valid = 0
    reached = False
    for held in itertools.count():
        if travelled(held, time) > dist:
            valid += 1
            reached = True
        elif reached:
            ans *= valid
            break

print(ans)