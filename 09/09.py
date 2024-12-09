def solve(fn, part2=False):
    with open(fn, 'r') as f:
        s = f.read().strip()

    a = list()
    f_id = 0
    a.extend([f_id,]*int(s[0]))
    for i in range(1, len(s), 2):
        f_id += 1
        a.extend([-1,]*int(s[i]))
        a.extend([f_id,]*int(s[i+1]))

    left = 0
    right = len(a)-1

    while True:
        while a[left] >= 0:
            left += 1
        while a[right] < 0:
            right -= 1
        if left >= right:
            break
        a[left], a[right] = a[right], a[left]

    checksum = 0
    for i in range(len(a)):
        if a[i] < 0:
            break
        checksum += i*a[i]
    return checksum

def main():
    assert solve('test.txt') == 1928
    print(solve('input.txt'))
    #assert solve('test.txt', part2=True) == 34
    #print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
