
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


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

        new_maze = []
        for i in range(len(maze)):
            if i in empty_rows:
                new_maze.append("." * (len(maze[0]) + len(empty_cols)))
            new_maze.append("")
            for j in range(len(maze[0])):
                if j in empty_cols:
                    new_maze[-1] += "."
                new_maze[-1] += maze[i][j]

        positions = []
        for i, row in enumerate(new_maze):
            for j, cell in enumerate(row):
                if cell == "#":
                    positions.append((i, j))

        total = 0
        for i, x in enumerate(positions):
            for j, y in enumerate(positions):
                if i >= j:
                    continue
                total += distance(x, y)
        print(total)

if __name__ == '__main__':
    main()
