import numpy as np

dirs = [(1,0), (0,1), (-1,0), (0,-1)]

def ascend(r, c, e, m, v):
    #position, elevation, map, visited
    #return number of 9s reachable from here
    if e == 9:
        return 1
    total = 0
    for dr, dc in dirs:
        r2 = r+dr
        c2 = c+dc
        if (v[r2, c2]==False) and (m[r2, c2] == e+1):
            v[r2, c2] = True
            total += ascend(r2, c2, e+1, m, v)
    return total


def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    m = np.array([[int(c) for c in li] for li in lines], dtype=np.int8)
    m = np.pad(m, 1, constant_values=-1)
    nr, nc = m.shape

    total = 0
    for r,c in np.ndindex(nr, nc):
        if m[r,c] == 0:
            v = np.zeros(m.shape, dtype=bool)
            total += ascend(r, c, 0, m, v)

    return total


if __name__ == '__main__':
    assert solve('test.txt') == 36
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 81
    #print(solve('input.txt', part2=True))
