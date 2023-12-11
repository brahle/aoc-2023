
def isdigit(x):
    return '0' <= x <= '9'


def is_symbol(x):
    return not isdigit(x) and x != '.'


dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
ds = len(dx)


def main():
    with open("03/input.txt") as f:
        lines = f.readlines()

    n = len(lines)
    m = len(lines[0]) - 1
    values = []
    gears = [[[] for i in range(m)] for j in range(n)]



    def check(x, y):
        if x < 0 or x >= n:
            return False
        if y < 0 or y >= m:
            return False
        if lines[x][y] == '*':
            gears[x][y].append(len(values))
        return is_symbol(lines[x][y])

    def check_part(i, j):
        checks = [check(i+dx[k], j+dy[k]) for k in range(ds)]
        return any(checks)

    i = 0
    while i < n:

        j = 0
        while j < m:

            if isdigit(lines[i][j]):
                is_part = check_part(i, j)
                val = int(lines[i][j])
                while isdigit(lines[i][j+1]):
                    j += 1
                    is_part |= check_part(i, j)
                    val = val * 10 + int(lines[i][j])
                values.append(val)
            j += 1
        i += 1

    print(values)
    print(gears)

    res = 0
    for i in range(n):
        for j in range(m):
            gears[i][j] = list(set(gears[i][j]))
            if len(gears[i][j]) == 2:
                print(i, j, gears[i][j], values[gears[i][j][0]], values[gears[i][j][1]])
                res += values[gears[i][j][0]] * values[gears[i][j][1]]
            elif gears[i][j]:
                print("IGNORED ", i, j, set(gears[i][j]))

    print(res)


if __name__ == '__main__':
    main()
