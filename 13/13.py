import math
from dataclasses import dataclass

@dataclass
class Button:
    dx: int
    dy: int

@dataclass
class Machine:
    a: Button
    b: Button
    px: int
    py: int

def parse_button(line):
    chunks = line.split()
    dx = int(chunks[2][2:-1])
    dy = int(chunks[3][2:])
    return Button(dx, dy)

def parse_machine(lines):
    a = parse_button(lines[0])
    b = parse_button(lines[1])
    chunks = lines[2].split()
    px = int(chunks[1][2:-1])
    py = int(chunks[2][2:])
    return Machine(a, b, px, py)

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    machines = list()
    for i in range(0, len(lines), 4):
        machines.append(parse_machine(lines[i:i+4]))

    min_cost = 0
    for m in machines:
        if part2:
            m.px += 10000000000000
            m.py += 10000000000000

        #print(m)
        na = 0
        int1 = m.px/m.b.dx
        int2 = m.py/m.b.dy
        slope1 = -m.a.dx/m.b.dx
        slope2 = -m.a.dy/m.b.dy
        if int1 > int2:
            top_int, bottom_int = int1, int2
            top_slope, bottom_slope = slope1, slope2
        else:
            top_int, bottom_int = int2, int1
            top_slope, bottom_slope = slope2, slope1

        na = (bottom_int-top_int)/(top_slope-bottom_slope)
        if abs(na-round(na)) > 1e-6:
            continue
        na = int(round(na))
        nb = na*top_slope + top_int
        if abs(nb-round(nb)) > 1e-6:
            continue
        nb = int(round(nb))
        if na < 0 or nb < 0:
            continue

        #print(na, nb)
        min_cost += 3*na + nb

    return min_cost

if __name__ == '__main__':
    assert solve('test.txt') == 480
    print(solve('input.txt'))
    #assert solve('test.txt', part2=True) == 1206
    #print(solve('test.txt', part2=True))
    print(solve('input.txt', part2=True))
