from dataclasses import dataclass
import numpy as np

dirs = [(1,0), (0,1), (-1,0), (0,-1)]

@dataclass
class RegionTally:
    area: int
    edges: int

def update_region_score_at(r, c, ch, m, v, t):
    #row, col, region-character, map, visited, tally
    v[r,c] = True
    t.area += 1
    for dr, dc in dirs:
        r2, c2 = r+dr, c+dc
        if m[r2,c2] != ch:
            t.edges += 1
        elif not v[r2, c2]:
            update_region_score_at(r2, c2, ch, m, v, t)


def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    m = np.array([list(li) for li in lines], dtype=np.chararray)
    v = np.zeros(m.shape, dtype=np.uint8)
    #pad edge with a fringe we don't need to visit
    m = np.pad(m, 1, constant_values='.')
    v = np.pad(v, 1, constant_values=1)
    
    total = 0
    for r, c in np.ndindex(m.shape):
        if not v[r,c]:
            tally = RegionTally(0,0)
            update_region_score_at(r, c, m[r,c], m, v, tally)
            total += (tally.area*tally.edges)

    return total

if __name__ == '__main__':
    assert solve('test1.txt') == 140
    assert solve('test2.txt') == 1930
    print(solve('input.txt'))
    assert solve('test2.txt', part2=True) == 1206
    #print(solve('input.txt', part2=True))
