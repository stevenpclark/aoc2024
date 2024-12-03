def score(s):
    total = 0
    chunks = s.split('mul(')
    for chunk in chunks:
        s = chunk.split(')')[0]
        try:
            args = [int(s2) for s2 in s.split(',')]
            if len(args) != 2:
                continue
            total += args[0]*args[1]
        except ValueError:
            pass
    return total

def solve(fn, part2=False):
    total = 0
    with open(fn) as f:
        s = ''.join(f.readlines())
    if part2:
        while s:
            off_ind = s.find("don't()")
            total += score(s[:off_ind])
            if off_ind < 0:
                #no more offs, we're done
                break
            s = s[off_ind:]
            on_ind = s.find("do()")
            if on_ind < 0:
                #no more ons, we're done
                break
            s = s[on_ind:]
    else:
        total += score(s)

    return total

def main():
    assert solve('test.txt') == 161
    print(solve('input.txt'))
    assert solve('test2.txt', part2=True) == 48
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
