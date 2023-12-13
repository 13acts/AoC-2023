from icecream import ic
import itertools
import re

U = '?'
X = '.'
O = '#'

PART = 1
STEP_DEBUG = False
P2_DEBUG = False

with open('data/12.txt') as f:
    lines = f.read().splitlines()
    layout = []
    if PART == 1:
        for line in lines:
            a, b = line.split()
            layout.append((a, [int(x) for x in b.split(',')]))

    if PART == 2:
        for line in lines:
            a, b = line.split()
            layout.append(('?'.join([a]*5), [int(x) for x in b.split(',')]*5))


def solve_line(symbols, guide):
    cache = []
    for i, frame in enumerate(frames(len(symbols), guide)):
        if STEP_DEBUG:
            ic(frame)
        cache += [valid_combinations(guide[i], frame, symbols[frame[0]:frame[1]+1])]
    
    if P2_DEBUG:
        ic(cache)

    validated = solve(cache, symbols, guide)

    if P2_DEBUG:
        print(validated)

    return validated


def is_aligned(combin, ref):
    '''
    Check if combin is aligned with ref (absolute check)
    '''
    for i in range(len(ref)):
        if (combin[i] == O and ref[i] == X) or (combin[i] == X and ref[i] == O):
            return False
    return True


def frames(total:int, numbers:list[int]) -> list:
    '''
    Absolute frame that a contig reside in, ie the contig cannot be outside of this frame.
    Find frame for a list of numbers reside in total length
    '''
    return [(sum(x+1 for x in numbers[:i]), total-1-sum(x+1 for x in numbers[i+1:])) for i in range(len(numbers))]


def valid_combinations(k:int, frame:tuple, ref:str) -> list:
    '''
    Combinations of k-mer in frame that itself is aligned to ref (primrary check)
    '''
    n = frame[1] - frame[0] + 1 - k
    result = []
    for i in range(n+1):
        if all(ref[j] in (U, O) for j in range(i, i+k)):
            result += [frame[0]+i]
    return result

            
    
def solve(cache, symbols, guide):
    count = 0
    def recur(curr_patch, previous_pos, n, log:list):
        '''
        Recursively find all possible combinations of starting positions in cache from left to right
        '''
        # Stopping condition: successfully get to the last item
        if curr_patch == len(guide):
            if P2_DEBUG:
                print(log,'found 1')
            
            # Final check if it's aligned with given data
            if is_aligned(index_to_string(log, guide, len(symbols)), symbols):
                n += 1
            return n
        
        # For each value in the current item
        for patch_pos in cache[curr_patch]:
            
            # Make sure flanking nodes are empty
            if patch_pos+guide[curr_patch] < len(symbols):
                flank = patch_pos-1, patch_pos+guide[curr_patch]
            else:
                flank = [patch_pos-1]

            # Make sure next node is separated from previous node and flanking nodes are empty
            if patch_pos > previous_pos+guide[curr_patch-1] and all(symbols[x] != O for x in flank):
                if P2_DEBUG:
                    ic(patch_pos)
                log += [patch_pos]
                n = recur(curr_patch+1, patch_pos, n, log)
                log.pop()    
        return n
    
    # Initiate recursion with flank check
    for x in cache[0]:
        if x != 0:
            flank = x-1, x+guide[0]
        else:
            flank = [x+guide[0]]
        if all(symbols[x] != O for x in flank):
            if P2_DEBUG:
                ic(x)        
            count += recur(1, x, 0, [x])
    
    return count


def index_to_string(log, guide, l):
    '''
    From a map of starting positions and contig length, return the final string
    '''
    string = [X] * l
    for i, v in enumerate(log):
        for j in range(v, v+guide[i]):
            string[j] = O
    return ''.join(string)



############ main() ###########################

# total = 0
# for symbols, guide in layout[:1]:
#     print(symbols)
#     total += solve_line(symbols, guide)

print(sum(solve_line(symbols, guide) for symbols, guide in layout))



############ DEBUG ############################

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
# print(solve_line('????.#????#?????#??#', [1,2,1,1,7]))

# print(solve_line('???.###????.###????.###????.###????.###', [1,1,3,1,1,3,1,1,3,1,1,3,1,1,3]))
# print(solve_line('?'.join(['?###????????']*5), [3,2,1]*5))


