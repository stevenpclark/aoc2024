from math import prod
import numpy as np

dirs = ((-1,-1),(-1,0),(-1,1),
        (0,-1),(0,1),
        (1,-1),(1,0),(1,1))

target = 'XMAS'

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    m = np.array([list(li) for li in lines], dtype=np.chararray)
    #pad matrix to simplify edge conditions
    m = np.pad(m, 3, constant_values='.')
    nr, nc = m.shape

    num_matches = 0
    for r, c in np.ndindex(nr, nc):
        ch = m[r,c]
        for dr, dc in dirs:
            found = True
            for i, x in enumerate(target):
                if m[r+i*dr,c+i*dc] != x:
                    found = False
                    break
            if found:
                num_matches += 1

    return num_matches


def main():
    assert solve('test.txt') == 18
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 9

if __name__ == '__main__':
    main()
