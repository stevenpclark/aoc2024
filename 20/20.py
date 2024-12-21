from collections import defaultdict
from queue import PriorityQueue
import numpy as np

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

#thanks to https://www.redblobgames.com/pathfinding/a-star/implementation.html
# for refreshing me on a-star

def heuristic(a, b):
    guess = abs(a[0]-b[0])+abs(a[1]-b[1])
    return guess

def solve(fn, min_shortcut_size, cheat_length):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    m = np.array([list(li) for li in lines], dtype=np.chararray)
    m = np.pad(m, 19, constant_values='#')

    rows, cols = np.where(m=='S')
    start = (rows[0], cols[0])

    rows, cols = np.where(m=='E')
    goal = (rows[0], cols[0])

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()[1]

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

    costs = np.zeros(m.shape)

    num_shortcuts = 0

    for r, c in np.ndindex(m.shape):
        if m[r,c] != '#':
            high_cost = cost_so_far[(r,c)]
            for dr in range(-cheat_length, cheat_length+1):
                for dc in range(-cheat_length, cheat_length+1):
                    dist = abs(dr)+abs(dc)
                    if dist > cheat_length:
                        continue
                    r2, c2 = r+dr, c+dc
                    if m[r2,c2] != '#':
                        cost2 = cost_so_far[(r2,c2)]
                        if cost2 >= high_cost:
                            continue
                        savings = high_cost-cost2-dist
                        if savings >= min_shortcut_size:
                            num_shortcuts += 1
    return num_shortcuts
    
if __name__ == '__main__':
    assert solve('test.txt', 36, 2) == 4
    print(solve('input.txt', 100, 2))
    assert solve('test.txt', 72, 20) == 29
    print(solve('input.txt', 100, 20))
