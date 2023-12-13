from icecream import ic
import itertools
import re

U = '?'
X = '.'
O = '#'

PART = 1
STEP_DEBUG = False

with open('data/12.txt') as f:
    lines = f.read().splitlines()
    layout = []
    if PART == 1:
        for line in lines:
            a, b = line.split()
            layout.append((a, list(map(int, b.split(',')))))

    if PART == 2:
        for line in lines:
            a, b = line.split()
            a = '?'.join([a]*5)
            b = list(map(int, b.split(',')))*5
            layout.append((a, b))


def solve_line(symbols, guide):
    cache = []
    for i, frame in enumerate(valid_frame(len(symbols), guide)):
        if STEP_DEBUG:
            ic(frame)
        cache += [valid_combinations(guide[i], frame, symbols[frame[0]:frame[1]+1])]
    
    ic(cache)
    # print(list(itertools.product(*cache)))

    ####### OPTIMIZED UP TO THIS POINT ##########
    # Some lines can have products len up to 10e+19

    validated = solve(cache, symbols, guide)

    return validated


def valid_snip(combin, ref):
    for i in range(len(ref)):
        if (combin[i] == O and ref[i] == X) or (combin[i] == X and ref[i] == O):
            return False
    return True


def valid_frame(total:int, numbers:list[int]) -> list:
    return [(sum(x+1 for x in numbers[:i]), total-1-sum(x+1 for x in numbers[i+1:])) for i in range(len(numbers))]


def valid_combinations(k:int, frame:tuple, ref:str) -> list:
    n = frame[1] - frame[0] + 1 - k
    result = []
    for i in range(n+1):
        if all(ref[j] in (U, O) for j in range(i, i+k)):
            result += [frame[0]+i]
    return result

			
	
def solve(cache, symbols, guide):
	n = 0
	def recur(curr_patch, previous_pos):
		if curr_patch == len(guide):
			n += 1
			return
		for patch_pos in cache[curr_patch]:
			if patch_pos > previous_pos+guide[curr_patch-1]:
				recur(curr_patch+1, curr_patch)
	for x in cache[0]:
		recur(1, x)
	return n
		
		
	
def valid_count(positions:list[tuple], guide:list[int], curr_patch:int, previous_pos:int):
	if curr_patch == len(guide):
		return
	
	this = []
	for patch_pos in positions[current_patch]:
		if patch_pos > previous_pos+guide[curr_patch-1]:
			this += [patch_pos]
			
	



# print(sum(solve_line(symbols, guide) for symbols, guide in layout))



############ DEBUG ############################

# assert solve_line('???.###', [1, 1, 3]) == 1
assert solve_line('.??..??...?##.', [1, 1, 3]) == 4
# assert solve_line('?###????????', [3, 2, 1]) == 10
# assert solve_line('?#?#?#?#?#?#?#?', [1, 3, 1, 6]) == 1
# assert solve_line('????.######..#####.', [1, 6, 5]) == 4
# assert solve_line('????.#...#...', [4,1,1]) == 1


# print(solve_line('??.?#??###', [1,6]))
# print(solve_line('?.?????#???#?',[1,1,2,2]))
# print(solve_line('??###?????????????', [4,2,1]))
# print(solve_line('?#?#?????.#..????', [3,3,1,1,1]))
# print(solve_line('?.???.?.?###??#', [2,7]))

# print(solve_line('???.###????.###????.###????.###????.###', [1,1,3,1,1,3,1,1,3,1,1,3,1,1,3]))
# print(solve_line('?'.join(['?###????????']*5), [3,2,1]*5))


