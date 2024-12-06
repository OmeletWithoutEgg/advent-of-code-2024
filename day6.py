with open('day6.in', 'r') as f:
    a = [list(line.strip()) for line in f.readlines()]

n = len(a)
m = len(a[0])
print(f'{n = } {m = }')

def in_grid(cur):
    _, i, j = cur
    return i >= 0 and i < n and j >= 0 and j < m

def get_next(cur):
    direction, i, j = cur
    dx, dy = {
            'v': (1, 0),
            '^': (-1, 0),
            '>': (0, 1),
            '<': (0, -1),
            }[direction]
    res = (direction, i + dx, j + dy)
    if not in_grid(res):
        return res
    if a[i + dx][j + dy] != '#':
        return res

    next_direction = {
            '>': 'v',
            'v': '<',
            '<': '^',
            '^': '>'
            }[direction]
    return (next_direction, i, j)

def find_init():
    for i in range(n):
        for j in range(m):
            if a[i][j] != '#' and a[i][j] != '.':
                return (a[i][j], i, j)


def part1():
    vis = set()
    cur = find_init()
    while in_grid(cur) and cur not in vis:
        vis.add(cur)
        cur = get_next(cur)

    vis_cell = set()
    for _, x, y in vis:
        vis_cell.add((x, y))
    print(len(vis_cell))
    return vis_cell

def part2(vis_cell):
    init = find_init()

    from tqdm import tqdm
    ans = 0
    for i, j in tqdm(vis_cell):
        save = a[i][j]

        a[i][j] = '#'

        vis = set()
        cur = init
        while in_grid(cur) and cur not in vis:
            vis.add(cur)
            cur = get_next(cur)
        if in_grid(cur):
            # not escaped
            ans += 1
        a[i][j] = save

    print(ans)

vis_cell = part1()
part2(vis_cell)
