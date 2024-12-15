import numpy as np

dir_map = {'^': (-1,0), '<': (0,-1), 'v': (1,0), '>': (0,1)}


def convert_line(li, part2):
    if part2:
        li = li.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    return list(li)

def move_horizontally(m, r, c, dc):
    ch = m[r,c]
    if ch == '.':
        return True
    elif ch == '#':
        return False
    elif ch in 'O@':
        if move_horizontally(m, r, c+dc, dc):
            m[r,c+dc] = ch
            m[r,c] = '.'
            return True
        else:
            return False
    else:
        assert ch in '[]'
        if move_horizontally(m, r, c+2*dc, dc):
            m[r,c+2*dc] = m[r,c+dc]
            m[r,c+dc] = ch
            m[r,c] = '.'
            return True
        else:
            return False

def can_move_vertically(m, r, c, dr):
    #here, m[r,c] == '['
    #only called for part2
    assert m[r,c] == '['
    ch_left = m[r+dr,c]
    ch_right = m[r+dr,c+1]
    if '#' in [ch_left, ch_right]:
        return False
    if ch_left == '[':
        return can_move_vertically(m, r+dr, c, dr)
    return (ch_left == '.' or can_move_vertically(m, r+dr, c-1, dr)) and (ch_right == '.' or can_move_vertically(m, r+dr, c+1, dr))


def move_vertically_no_check(m, r, c, dr):
    #here, m[r,c] == '['
    #only called for part2
    assert m[r,c] == '['
    ch_left = m[r+dr,c]
    ch_right = m[r+dr,c+1]
    if ch_left == '[':
        move_vertically_no_check(m, r+dr, c, dr)
    else:
        if ch_left == ']':
            move_vertically_no_check(m, r+dr, c-1, dr)
        if ch_right == '[':
            move_vertically_no_check(m, r+dr, c+1, dr)
    m[r+dr,c:c+2] = ['[', ']']
    m[r,c:c+2] = ['.', '.']


def move_vertically(m, r, c, dr):
    ch = m[r,c]
    if ch == '.':
        return True
    elif ch == '#':
        return False
    elif ch in 'O@':
        if move_vertically(m, r+dr, c, dr):
            m[r+dr,c] = ch
            m[r,c] = '.'
            return True
        else:
            return False
    elif ch == ']':
        c -= 1
        ch = m[r,c]
    assert ch == '['
    if can_move_vertically(m, r, c, dr):
        move_vertically_no_check(m, r, c, dr)
        return True
    else:
        return False

def solve(fn, part2=False):
    with open(fn, 'r') as f:
        lines = f.read().splitlines()

    empty = lines.index('')

    map_lines = [convert_line(li, part2) for li in lines[0:empty]]

    m = np.array(map_lines, dtype=np.chararray)
    moves = ''.join(lines[empty+1:])

    rows, cols = np.where(m=='@')
    r, c = rows[0],cols[0]

    for move in moves:
        #print(move)
        dr, dc = dir_map[move]

        if dr:
            if not move_vertically(m, r, c, dr):
                continue
        else:
            if not move_horizontally(m, r, c, dc):
                continue

        r += dr
        c += dc

    if not part2:
        rows, cols = np.where(m=='O')
    else:
        rows, cols = np.where(m=='[')

    return sum(100*rows + cols)

if __name__ == '__main__':
    assert solve('test1.txt') == 2028
    assert solve('test2.txt') == 10092
    print(solve('input.txt'))
    assert solve('test2.txt', part2=True) == 9021
    print(solve('input.txt', part2=True))
