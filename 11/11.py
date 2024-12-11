from collections import Counter

def evolve(n):
    if n==0:
        return [1,]
    else:
        s = str(n)
        s_len = len(s)
        if s_len%2==0:
            return [int(s[:s_len//2]), int(s[s_len//2:])]
    return [2024*n,]

def solve(fn, num_blinks=25):
    with open(fn, 'r') as f:
        s = f.read()

    c = Counter([int(s2) for s2 in s.split()])

    for i in range(num_blinks):
        c2 = Counter()
        for k,count in c.items():
            for k2 in evolve(k):
                c2[k2] += count
        c = c2

    return sum(c.values())

if __name__ == '__main__':
    assert solve('test.txt') == 55312
    print(solve('input.txt'))
    print(solve('input.txt', num_blinks=75))
