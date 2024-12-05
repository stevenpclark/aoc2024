def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    rules = list()
    updates = list()
    done_rules = False
    for li in lines:
        if not done_rules:
            if li:
                rules.append([int(s) for s in li.split('|')])
            else:
                done_rules = True
        else:
            updates.append([int(s) for s in li.split(',')])

    total = 0
    for up in updates:
        update_valid = True
        for a, b in rules:
            try:
                a_ind, b_ind = up.index(a), up.index(b)
            except ValueError:
                continue
            if a_ind >= b_ind:
                update_valid = False
                break
        if update_valid:
            total += up[len(up)//2]

    return total


def main():
    assert solve('test.txt') == 143
    print(solve('input.txt'))

if __name__ == '__main__':
    main()
