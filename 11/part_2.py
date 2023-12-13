BONUS = 1000000

def axis_distance(a, b, empty):
    if a > b:
        a, b = b, a
    cnt = sum(1 for i in range(a + 1, b) if i in empty)
    return abs(b - a) + cnt * (BONUS - 1)

def distance(a, b, empty_rows, empty_cols):
    return axis_distance(a[0], b[0], empty_rows) + axis_distance(a[1], b[1], empty_cols)


def main():
    with open("11/input.txt") as f:
        maze = [x.strip() for x in f.readlines()]

        empty_rows = []
        empty_cols = []

        for i in range(len(maze)):
            if maze[i] == "." * len(maze[i]):
                empty_rows.append(i)

        for j in range(len(maze[0])):
            if all(maze[i][j] == "." for i in range(len(maze))):
                empty_cols.append(j)

        # dist = []
        # for i in range(len(maze)):
        #     dist.append([])
        #     for j in range(len(maze[0])):
        #         if i in empty_rows or j in empty_cols:
        #             dist[-1].append(2)
        #         else:
        #             dist[-1].append(1)

        positions = []
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                if cell == "#":
                    positions.append((i, j))

        total = 0
        for i, x in enumerate(positions):
            for j, y in enumerate(positions):
                if i >= j:
                    continue
                total += distance(x, y, empty_rows, empty_cols)
        print(total)


if __name__ == '__main__':
    main()
