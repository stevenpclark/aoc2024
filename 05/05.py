def sort_and_score(update, rules):
    #there's almost certainly a smarter way of doing this, but eh, whatever
    valid = False
    while not valid:
        valid = True
        for a, b in rules:
            try:
                a_ind, b_ind = update.index(a), update.index(b)
            except ValueError:
                continue
            if a_ind >= b_ind:
                #move b to just after a
                update.insert(a_ind+1, update.pop(b_ind))
                valid = False
    return update[len(update)//2]


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
    for update in updates:
        update_valid = True
        for a, b in rules:
            try:
                a_ind, b_ind = update.index(a), update.index(b)
            except ValueError:
                continue
            if a_ind >= b_ind:
                update_valid = False
                break
        if update_valid and not part2:
            total += update[len(update)//2]
        if not update_valid and part2:
            total += sort_and_score(update, rules)

    return total


def main():
    assert solve('test.txt') == 143
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 123
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
