from dataclasses import dataclass
import numpy as np

dirs = [(1,0), (0,1), (-1,0), (0,-1)]

@dataclass
class RegionTally:
    area: int
    edges: int

def update_region_score_at(r, c, ch, m, v, edges, t, part2, v_list):
    #row, col, region-character, map, visited, edges, tally
    v[r,c] = True
    v_list.append((r,c))
    t.area += 1
    for i, d in enumerate(dirs):
        dr, dc = d
        r2, c2 = r+dr, c+dc
        if m[r2,c2] != ch:
            edges[r, c, i] = 1
            t.edges += 1
        elif not v[r2, c2]:
            update_region_score_at(r2, c2, ch, m, v, edges, t, part2, v_list)

    return v_list


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
            edges = np.zeros((m.shape[0], m.shape[1], 4), dtype=np.uint8)
            tally = RegionTally(0,0)
            v_list = list()
            v_list = update_region_score_at(r, c, m[r,c], m, v, edges, tally, part2, v_list)
            if part2:
                for r2, c2 in v_list:
                    for i in range(4):
                        if edges[r2, c2, i]:
                            dr, dc = dirs[(i+1)%2]
                            if edges[r2+dr, c2+dc, i]:
                                tally.edges -= 1
            total += (tally.area*tally.edges)

    return total

if __name__ == '__main__':
    assert solve('test1.txt') == 140
    assert solve('test2.txt') == 1930
    print(solve('input.txt'))
    assert solve('test2.txt', part2=True) == 1206
    print(solve('input.txt', part2=True))
