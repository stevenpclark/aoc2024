from dataclasses import dataclass
import numpy as np

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

        c = np.array([[m.a.dx, m.b.dx], [m.a.dy, m.b.dy]])
        d = np.array([m.px, m.py])

        na, nb = np.linalg.solve(c,d)

        na = int(round(na))
        nb = int(round(nb))

        if na<0 or nb<0:
            continue

        if na*m.a.dx + nb*m.b.dx != m.px:
            continue

        if na*m.a.dy + nb*m.b.dy != m.py:
            continue

        #print(na, nb)
        min_cost += 3*na + nb

    print(min_cost)
    return min_cost

if __name__ == '__main__':
    assert solve('test.txt') == 480
    print(solve('input.txt'))
    print(solve('input.txt', part2=True))
