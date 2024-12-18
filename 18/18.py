from collections import defaultdict
from queue import PriorityQueue
import numpy as np

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

#thanks to https://www.redblobgames.com/pathfinding/a-star/implementation.html
# for refreshing me on a-star

def heuristic(a, b):
    guess = abs(a[0]-b[0])+abs(a[1]-b[1])
    return guess

def solve(fn, sz, num_bytes, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()


    byte_locs = list()
    for li in lines:
        byte_locs.append(tuple(int(s) for s in li.split(',')))

    m = np.array([list('.'*sz) for i in range(sz)], dtype=np.chararray)
    m = np.pad(m, 1, constant_values='#')

    for x,y in byte_locs[:num_bytes]:
        m[y+1,x+1] = '#'

    start = (1,1)
    goal = (sz, sz)

    while True:
        #part2 could be greatly accelerated by reusing data from prev iterations
        #but, fast enough for now.
        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()[1]

            if current == goal:
                break

            neighbors = list()
            r,c = current
            for dr, dc in dirs:
                r2, c2 = r+dr, c+dc
                if m[r2,c2] != '#':
                    neighbors.append((r2,c2))

            for i, adj in enumerate(neighbors):
                new_cost = cost_so_far[current] + 1
                visited_previously = adj in cost_so_far
                if not visited_previously or new_cost < cost_so_far[adj]:
                    cost_so_far[adj] = new_cost
                    priority = new_cost + heuristic(adj, goal)
                    frontier.put((priority, adj))
                    came_from[adj] = current

        cost = cost_so_far.get(goal, -1)
        if part2 == False:
            print(cost)
            return cost
        else:
            if cost < 0:
                fatal_byte = byte_locs[num_bytes-1]
                print(fatal_byte)
                return fatal_byte
            else:
                #add a new byte
                x,y = byte_locs[num_bytes]
                num_bytes += 1
                m[y+1,x+1] = '#'
                print(num_bytes)


if __name__ == '__main__':
    assert solve('test.txt', 7, 12) == 22
    print(solve('input.txt', 71, 1024))
    assert solve('test.txt', 7, 12, part2=True) == (6,1)
    solve('input.txt', 71, 1024, part2=True)
