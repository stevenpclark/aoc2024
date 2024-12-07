from itertools import product
from operator import add, mul

def concat(a, b):
    return int(f'{a}{b}')

def solve(fn, part2=False):
    if part2:
        all_ops = [add, mul, concat]
    else:
        all_ops = [add, mul]

    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    total = 0

    for li in lines:
        s1, s2 = li.split(':')
        target = int(s1)
        args = [int(s) for s in s2.split()]
        num_ops_to_use = len(args)-1

        op_trials = list(product(all_ops, repeat=num_ops_to_use))
        for op_trial in op_trials:
            r = args[0]
            for i, op in enumerate(op_trial):
                r = op(r, args[i+1])
            if r == target:
                total += target
                break

    return total


def main():
    assert solve('test.txt') == 3749
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 11387
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
