from functools import cache

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    parts = lines[0].split(', ')
    targets = lines[2:]

    @cache
    def num_possible(target):
        if not target:
            return 0
        total = 0
        for p in parts:
            if p == target:
                total += 1
            elif target.startswith(p):
                total += num_possible(target[len(p):])
        return total

    if not part2:
        return sum(num_possible(target)>0 for target in targets)
    else:
        return sum(num_possible(target) for target in targets)

if __name__ == '__main__':
    assert solve('test.txt') == 6
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 16
    print(solve('input.txt', part2=True))
