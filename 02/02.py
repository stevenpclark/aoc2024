import numpy as np

def is_safe(arr, part2=False):
    deltas = np.diff(arr)
    num_neg = sum(deltas<0)
    if num_neg >= 2:
        deltas *= -1
    bools = (deltas>=1) & (deltas<=3)
    if not part2:
        return bools.all()
    else:
        num_ok = sum(bools)
        if num_ok == len(bools):
            return True
        if num_ok < len(bools)-2:
            return False
        for i, d in enumerate(deltas):
            if not bools[i]:
                #this is the only problematic delta
                if i==0 or i==len(bools)-1:
                    #failures at either end are fine
                    return True
                d_left = deltas[i]+deltas[i-1]
                d_right = deltas[i]+deltas[i+1]
                return 1<=d_left<=3 or 1<=d_right<=3

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
