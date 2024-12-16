from queue import PriorityQueue
import numpy as np

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

transition_costs = [1000, 1000, 1]

#keep track of deer pos as (row, col, dir_ind) tuple

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
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()[1]

        if current[:2] == goal[:2]: #orientation doesn't matter
            break

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
            if adj not in cost_so_far or new_cost < cost_so_far[adj]:
                cost_so_far[adj] = new_cost
                priority = new_cost + heuristic(adj, goal)
                frontier.put((priority, adj))
                came_from[adj] = current

    costs = list()
    for i in range(4):
        g = goal[:2]+(i,)
        if g in cost_so_far:
            costs.append(cost_so_far[g])

    #prev = came_from[current]
    #while prev:
        #m[prev[0], prev[1]] = 'O'
        #prev = came_from[prev]
    #print(m)

    return min(costs)

if __name__ == '__main__':
    assert solve('test1.txt') == 7036
    assert solve('test2.txt') == 11048
    print(solve('input.txt'))
    #assert solve('test2.txt', part2=True) == 9021
    #print(solve('input.txt', part2=True))
