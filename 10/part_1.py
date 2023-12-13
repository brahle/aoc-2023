
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


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.n = len(maze)
        self.m = len(maze[0])
        self.distance = [[-1 for __ in range(self.m)] for _ in range(self.n)]

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

    def find_cycle_length(self):
        q = [self.start]
        self.distance[self.start[0]][self.start[1]] = 0
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


def main():
    maze = []
    with open('10/input.txt') as f:
        maze = Maze([line.strip() for line in f])
    start = maze.fix_start()
    cycle = maze.find_cycle_length()
    print(cycle)


if __name__ == '__main__':
    main()
