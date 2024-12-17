from collections import defaultdict
from queue import PriorityQueue
import numpy as np

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

transition_costs = [1000, 1000, 1]

#keep track of deer pos as (row, col, dir_ind) tuple

#thanks to https://www.redblobgames.com/pathfinding/a-star/implementation.html
# for refreshing me on a-star

def heuristic(a, b):
    guess = abs(a[0]-b[0])+abs(a[1]-b[1])
    if a[2] in [1,2]:
        guess += 1000
    return guess

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    m = np.array([list(li) for li in lines], dtype=np.chararray)

    rows, cols = np.where(m=='S')
    start = (rows[0], cols[0], 0)

    rows, cols = np.where(m=='E')
    goal = (rows[0], cols[0], 0)
    goal2 = (rows[0], cols[0], 3)

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = defaultdict(list) #keep track of ALL best ways to get to a node
    cost_so_far = dict()
    came_from[start] = list()
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()[1]

        #if current[:2] == goal[:2]: #orientation doesn't matter
            #break

        neighbors = list() #can transition to either 2 or 3 other states
        r,c,dir_ind = current
        neighbors.append((r,c,(dir_ind+1)%4))
        neighbors.append((r,c,(dir_ind-1)%4))
        dr, dc = dirs[dir_ind]
        r2, c2 = r+dr, c+dc
        if m[r2,c2] != '#':
            neighbors.append((r2,c2,dir_ind))

        for i, adj in enumerate(neighbors):
            new_cost = cost_so_far[current] + transition_costs[i]
            visited_previously = adj in cost_so_far
            if not visited_previously or new_cost < cost_so_far[adj]:
                cost_so_far[adj] = new_cost
                priority = new_cost + heuristic(adj, goal)
                frontier.put((priority, adj))
                came_from[adj].append(current)
            elif new_cost == cost_so_far[adj]:
                came_from[adj].append(current)

    costs = list()
    for g in [goal, goal2]:
        if g in cost_so_far:
            costs.append(cost_so_far[g])
    min_cost = min(costs)

    trace = list()
    for g in [goal, goal2]:
        if g in cost_so_far:
            if cost_so_far[g] == min_cost:
                trace.extend(came_from[g])
    m[goal[0],goal[1]] = 'O'
    while trace:
        prev = trace.pop()
        m[prev[0], prev[1]] = 'O'
        trace.extend(came_from[prev])
    #print(m)
    best_count = np.sum(m=='O')
    #print(best_count)

    return (min_cost, best_count)

if __name__ == '__main__':
    assert solve('test1.txt') == (7036, 45)
    assert solve('test2.txt') == (11048, 64)
    print(solve('input.txt'))
    #assert solve('test2.txt', part2=True) == 9021
    #print(solve('input.txt', part2=True))
