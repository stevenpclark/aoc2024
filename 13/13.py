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
    print(machines[1])

    min_costs = list()
    for m in machines:
        min_cost = 1e6

        for na in range(100):
            for nb in range(100):
                if (na*m.a.dx + nb*m.b.dx == m.px) and (na*m.a.dy + nb*m.b.dy == m.py):
                    cost = 3*na + nb
                    min_cost = min(cost, min_cost)
        if min_cost != 1e6:
            min_costs.append(min_cost)

    return sum(min_costs)

if __name__ == '__main__':
    assert solve('test.txt') == 480
    print(solve('input.txt'))
    #assert solve('test.txt', part2=True) == 1206
    #print(solve('input.txt', part2=True))
