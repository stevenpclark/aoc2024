import numpy as np
from itertools import combinations

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    #7 lines, then an empty line
    keys = list()
    locks = list()
    for i in range(0, len(lines), 8):
        m = np.array([list(li) for li in lines[i:i+7]], dtype=str)
        heights = [int(x)-1 for x in np.sum(m=='#', axis=0)]
        is_lock = ''.join(m[0,:]) == '#####'
        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)

    num_fit = 0
    for h1 in keys:
        for h2 in locks:
            for i in range(len(h1)):
                if h1[i]+h2[i] > 5:
                    break
            else:
                num_fit += 1

    print(num_fit)
    return num_fit



    
if __name__ == '__main__':
    assert solve('test.txt') == 3
    print(solve('input.txt'))
    #assert solve('test.txt', part2=True) == 'co,de,ka,ta'
    #print(solve('input.txt', part2=True))
