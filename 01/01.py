
def solve(fn, part2=False):
    with open(fn) as f:
        lines = f.readlines()

    a = list()
    b = list()

    for li in lines:
        pair = [int(s) for s in li.split()]
        a.append(pair[0])
        b.append(pair[1])

    a.sort()
    b.sort()

    total = 0
    for i in range(len(a)):
        if not part2:
            total += abs(a[i]-b[i])
        else:
            total += a[i]*b.count(a[i])

    return total

def main():
    assert solve('test.txt') == 11
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 31
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
