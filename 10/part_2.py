
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
VALID_MOVES = [
    "-J7",
    "|7F",
    "-LF",
    "|LJ",
]
ds = len(dx)

OPTIONS = {
    (0, 1): "7",
    (0, 2): "-",
    (0, 3): "J",
    (1, 2): "F",
    (1, 3): "|",
    (2, 3): "L",
}

EXTENSIONS = {
    ".": [
        "...",
        "...",
        "...",
    ],
    "7": [
        "...",
        "-7.",
        ".|.",
    ],
    "|": [
        ".|.",
        ".|.",
        ".|.",
    ],
    "-": [
        "...",
        "---",
        "...",
    ],
    "L": [
        ".|.",
        ".L-",
        "...",
    ],
    "F": [
        "...",
        ".F-",
        ".|.",
    ],
    "J": [
        ".|.",
        "-J.",
        "...",
    ],
}


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.n = len(maze)
        self.m = len(maze[0])
        self.distance = [[-1 for __ in range(self.m)] for _ in range(self.n)]
        self.inside = [[True for __ in range(self.m)] for _ in range(self.n)]

    def is_in(self, point):
        x, y = point
        return 0 <= x < self.n and 0 <= y < self.m

    def fix_start(self):
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                if cell == 'S':
                    start = (i, j)

        valid = []
        for i in range(ds):
            x, y = start
            x += dx[i]
            y += dy[i]
            opposite_move = (i + 2) % ds
            if self.is_in((x, y)) and self[(x, y)] in VALID_MOVES[opposite_move]:
                valid.append(i)
        missing = OPTIONS[(valid[0], valid[1])]
        self.maze[start[0]] = self.maze[start[0]].replace('S', missing)

        self.start = start
        return start

    def __getitem__(self, point):
        x, y = point
        return self.maze[x][y]

    def find_cycle_length(self, start=None):
        if start is None:
            start = self.start
        q = [start]
        self.distance[start[0]][start[1]] = 0
        while q:
            x, y = q.pop(0)
            for i in range(ds):
                nx, ny = x + dx[i], y + dy[i]
                if self.is_in((nx, ny)) and self.distance[nx][ny] == -1 and self[(x, y)] in VALID_MOVES[i]:
                    self.distance[nx][ny] = self.distance[x][y] + 1
                    q.append((nx, ny))

        for row in self.distance:
            print(row)
        return max((max(d) for d in self.distance))

    def zoom_out(self) -> "Maze":
        new_maze = []
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                extension = EXTENSIONS[cell]
                for k, ext_row in enumerate(extension):
                    if i * 3 + k >= len(new_maze):
                        new_maze.append("")
                    new_maze[i * 3 + k] += ext_row
        return Maze(new_maze)

    def find_outside(self):
        q = [(0, 0)]
        self.inside[0][0] = False
        while q:
            x, y = q.pop(0)
            for i in range(ds):
                nx, ny = x + dx[i], y + dy[i]
                if self.is_in((nx, ny)) and self.inside[nx][ny] and self.distance[nx][ny] == -1:
                    self.inside[nx][ny] = False
                    q.append((nx, ny))

        cnt = 0
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                if not self.inside[i][j]:
                    print('.', end='')
                elif self.distance[i][j] != -1:
                    print('#', end='')
                elif i % 3 == 1 and j % 3 == 1:
                    print("+", end='')
                    cnt += 1
                else:
                    print("O", end='')
            print()

        return cnt

def main():
    maze = []
    with open('10/input.txt') as f:
        maze = Maze([line.strip() for line in f])
    start = maze.fix_start()
    cycle = maze.find_cycle_length()

    extended = maze.zoom_out()

    for row in extended.maze:
        print(row)

    larger_cycle = extended.find_cycle_length((start[0] * 3 + 1, start[1] * 3 + 1))
    res = extended.find_outside()
    print(res)


if __name__ == '__main__':
    main()
