import numpy as np

def is_safe(arr, part2=False):
    deltas = np.diff(arr)
    num_neg = sum(deltas<0)
    if num_neg >= 2:
        deltas *= -1
    if not part2:
        return ((deltas>=1) & (deltas<=3)).all()
    else:
        arr = list(arr)
        for i in range(len(arr)):
            if is_safe(arr[:i]+arr[i+1:]):
                return True
        return False


def solve(fn, part2=False):
    num_safe = 0
    with open(fn) as f:
        for li in f:
            arr = np.array([int(s) for s in li.split()])
            if is_safe(arr, part2):
                num_safe += 1

    return num_safe

def main():
    assert solve('test.txt') == 2
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 4
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
