from dataclasses import dataclass
import numpy as np

dirs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int


def parse_robot(line):
    line = line.replace('=', ',').replace(' ', ',')
    chunks = line.split(',')
    x = int(chunks[1])
    y = int(chunks[2])
    dx = int(chunks[4])
    dy = int(chunks[5])
    return Robot(x, y, dx, dy)


def solve(fn, nx, ny, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    robots = [parse_robot(li) for li in lines]

    if part2:
        lim = 10000
    else:
        lim = 100

    peak = 0
    for i in range(lim):
        m = np.zeros((ny, nx),dtype=np.uint8)
        for r in robots:
            r.x = (r.x+r.dx)%nx
            r.y = (r.y+r.dy)%ny
            m[r.y,r.x] = 1

        if part2:
            num_neighbors = 0
            for r in robots:
                for dx, dy in dirs:
                    if m[(r.y+dy)%ny,(r.x+dx)%nx]:
                        num_neighbors += 1

            if num_neighbors > peak:
                #look for sudden jump in num_neighbors
                print(i+1, num_neighbors)
                peak = num_neighbors
                np.savetxt(f'vis.txt', m, fmt="%1d", delimiter='')


    quads = np.zeros((2,2), dtype=np.int32)
    for r in robots:
        x = -1
        y = -1
        if r.x < nx//2:
            x = 0
        elif r.x > nx//2:
            x = 1
        if r.y < ny//2:
            y = 0
        elif r.y > ny//2:
            y = 1
        if x >= 0 and y >= 0:
            quads[y,x] += 1

    return np.product(quads)

if __name__ == '__main__':
    assert solve('test.txt', 11, 7) == 12
    print(solve('input.txt', 101, 103))
    solve('input.txt', 101, 103, part2=True)
