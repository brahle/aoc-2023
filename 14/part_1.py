
def main():
    with open("14/input.txt") as f:
        platform = []
        for line in f:
            platform.append(line.strip())

        n = len(platform)
        m = len(platform[0])
        heights = [n for i in range(m)]

        res = 0
        for i in range(n):
            for j in range(m):
                if platform[i][j] == "#":
                    heights[j] = n - i - 1
                if platform[i][j] == "O":
                    res += heights[j]
                    heights[j] -= 1

        print(res)


if __name__ == '__main__':
    main()
