from dataclasses import dataclass

@dataclass
class DiskFile:
    f_id: int
    start: int
    length: int

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        s = f.read().strip()

    a = list()
    files = list()
    f_id = 0
    start = 0
    for i,c in enumerate(s):
        length = int(c)
        if i % 2 == 0:
            f = DiskFile(f_id, start, length)
            f_id += 1
        else:
            f = DiskFile(-1, start, length)
        start += length
        files.append(f)
        a.extend([f.f_id,]*f.length)

    if not part2:
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
    else:
        right = len(files)-1

        while right > 0:
            f = files[right]
            left = 1
            while files[left].f_id >= 0 or files[left].length < f.length:
                left += 2
                if left >= right:
                    break
            if left < right:
                #right is file, left is space
                #first zero out file
                space = files[left]
                a[f.start:f.start+f.length] = [-1,]*f.length
                #transfer file
                f.start = space.start
                a[f.start:f.start+f.length] = [f.f_id,]*f.length
                #update space
                space.length -= f.length
                space.start += f.length

            right -= 2

    checksum = 0
    for i in range(len(a)):
        if a[i] < 0:
            continue
        checksum += i*a[i]
    return checksum

def main():
    assert solve('test.txt') == 1928
    print(solve('input.txt'))
    assert solve('test.txt', part2=True) == 2858
    print(solve('input.txt', part2=True))

if __name__ == '__main__':
    main()
