from math import gcd
import numpy as np
from itertools import combinations

def add_if_on_grid(p, m, s):
    nr, nc = m.shape
    r, c = p
    if 0<=r<nr and 0<=c<nc:
        s.add((r,c))
        return True
    return False

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    m = np.array([list(li) for li in lines], dtype=np.chararray)

    anti_loc_set = set()

    unique_chars = np.unique(m)
    for ch in unique_chars:
        if ch == '.':
            continue
        locs = [np.array(x) for x in zip(*np.where(m==ch))]
        for a,b in combinations(locs, 2):
            d = a-b
            if not part2:
                add_if_on_grid(a+d, m, anti_loc_set)
                add_if_on_grid(b-d, m, anti_loc_set)
            else:
                d = d//gcd(*d)
                p = np.copy(a)
                while add_if_on_grid(p, m, anti_loc_set):
                    p += d
                p = a - d
                while add_if_on_grid(p, m, anti_loc_set):
                    p -= d

    return len(anti_loc_set)

def main():
    assert solve('test.txt') == 14
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 34
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
