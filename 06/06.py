import numpy as np

dirs = ((-1,0), (0,1), (1,0), (0,-1))

def can_escape(m, part2=False):
    #return number of pos visited, or -1 if no escape

    nr, nc = m.shape
    if part2:
        v_shape = (nr, nc, 4)
    else:
        v_shape = (nr, nc, 1)
    visited = np.zeros(v_shape, dtype=bool)

    r, c = [int(x) for x in np.where(m=='^')]
    dir_ind = 0
    dr, dc = dirs[dir_ind]

    while True:
        if part2:
            v_ind = dir_ind
        else:
            v_ind = 0
        if visited[r,c,v_ind] and part2:
            #we're looping forever
            return -1
        visited[r,c,v_ind] = True
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

    return np.sum(visited)

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    m = np.array([list(li) for li in lines], dtype=np.chararray)

    if not part2:
        return can_escape(m, part2)
    else:
        num_traps = 0
        for r, c in np.ndindex(m.shape):
            if m[r,c] == '.':
                m[r,c] = '#'
                if can_escape(m, part2) < 0:
                    num_traps += 1
                m[r,c] = '.'
        return num_traps


def main():
    assert solve('test.txt') == 41
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 6
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
