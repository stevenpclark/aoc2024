import numpy as np

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    m = np.array([list(li) for li in lines], dtype=np.chararray)
    unique_chars = np.unique(m)
    m = np.pad(m, 1, constant_values='.')

    
    for ch in unique_chars:
        m2 = (m==ch)
        print(m2)
        #locs = [np.array(x) for x in zip(*np.where(m==ch))]

    return 0

def main():
    assert solve('test1.txt') == 140
    assert solve('test2.txt') == 1930
    print(solve('input.txt'))
    #assert solve('test.txt', part2=True) == 34
    #print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
