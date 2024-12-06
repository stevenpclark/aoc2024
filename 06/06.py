import numpy as np

dirs = ((-1,0), (0,1), (1,0), (0,-1))

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    m = np.array([list(li) for li in lines], dtype=np.chararray)
    nr, nc = m.shape

    r, c = [int(x) for x in np.where(m=='^')]
    dir_ind = 0
    dr, dc = dirs[dir_ind]

    while True:
        m[r,c] = 'X'
        r2 = r+dr
        c2 = c+dc
        if r2<0 or r2>=nr or c2<0 or c2>=nc:
            #we are stepping off
            break
        if m[r2,c2] == '#':
            dir_ind = (dir_ind+1)%4
            dr, dc = dirs[dir_ind]
            continue
        r,c = r2,c2

    return np.count_nonzero(m=='X')


def main():
    assert solve('test.txt') == 41
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 6
    #print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
