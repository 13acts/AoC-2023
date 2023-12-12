from icecream import ic
from collections import defaultdict
import itertools
import math
import re

U = '?'
X = '.'
O = '#'

STEP_DEBUG = False

with open('data/12.txt') as f:
    lines = f.read().splitlines()
    layout = []
    for line in lines:
        a, b = line.split()
        layout.append((a, list(map(int, b.split(',')))))

# with open('log.txt', 'w') as f:
#     f.close()

# ic(layout)

def solve_line(symbols, guide):
    # print(symbols, guide)
    cache = []
    for i, frame in enumerate(valid_frame(len(symbols), guide)):
        tmp = []
        # print()
        # symbols1 = symbols
        if STEP_DEBUG:
            ic(frame)
        # for j, combin in enumerate(valid_combinations(guide[i], frame, symbols1[frame[0]:frame[1]+1])):
        #     print(combin)
        #     if STEP_DEBUG:
        #         ic(combin)
        #     # if valid_snip(combin, symbols1[frame[0]:frame[1]+1]):
        #     #     if STEP_DEBUG:
        #     #         ic(True)
        #     tmp += [frame[0]+j]
        # cache[i] = (guide[i], tmp)
        cache += [valid_combinations(guide[i], frame, symbols[frame[0]:frame[1]+1])]
    
    # ic(cache)
    # print(list(itertools.product(*cache)))

    validated = set()
    for tuple in itertools.product(*cache):
        combin = [X] * len(symbols)
        for i, pos in enumerate(tuple):
            for k in range(pos, pos+guide[i]):
                combin[k] = O
        combin = ''.join(combin)

        if STEP_DEBUG:
            ic(combin)
        if combin not in validated and list(map(len, re.findall(r'(#+)', combin))) == guide and valid_snip(combin, symbols):
            if STEP_DEBUG:
                ic(True)
            validated.add(combin)

    # print(len(validated))
    # with open('log.txt', 'a') as f:
    #     f.write(f'{len(validated)}\n')    

    return len(validated)


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
        
        # combin = X*i + O*k + X*(n-i)
        # for j in range(i, i+k):
        #     if (combin[j] == O and ref[j] == X) or (combin[j] == X and ref[j] == O):
        #         continue
        #     else:
        #         result += [frame[0]+i]

        
        if all(ref[j] in (U, O) for j in range(i, i+k)):
            # result += [X*i + O*k + X*(n-i)]
            result += [frame[0]+i]
    return result


# assert solve_line('???.###', [1, 1, 3]) == 1
# assert solve_line('.??..??...?##.', [1, 1, 3]) == 4
# assert solve_line('?###????????', [3, 2, 1]) == 10
# assert solve_line('?#?#?#?#?#?#?#?', [1, 3, 1, 6]) == 1
# assert solve_line('????.######..#####.', [1, 6, 5]) == 4
# assert solve_line('????.#...#...', [4,1,1]) == 1


# print(solve_line('??.?#??###', [1,6]))
# print(solve_line('?.?????#???#?',[1,1,2,2]))
# print(solve_line('??###?????????????', [4,2,1]))
# print(solve_line('?#?#?????.#..????', [3,3,1,1,1]))
# print(solve_line('?.???.?.?###??#', [2,7]))

print(sum(solve_line(symbols, guide) for symbols, guide in layout))
