
def get_hash(platform):
    return hash("\n".join(["".join(row) for row in platform]))


def north(platform):
    n = len(platform)
    m = len(platform[0])
    heights = [0 for i in range(m)]

    new_platform = []
    for i in range(n):
        new_platform.append([])

        for j in range(m):
            if platform[i][j] == "#":
                heights[j] = i + 1
                new_platform[i].append("#")
            elif platform[i][j] == "O":
                new_platform[i].append(".")
                new_platform[heights[j]][j] = "O"
                heights[j] += 1
            else:
                new_platform[i].append(".")
    return new_platform


def eval(platform):
    n = len(platform)
    m = len(platform[0])

    res = 0
    for i in range(n):
        for j in range(m):
            if platform[i][j] == "O":
                res += n - i
    return res


def rotate(platform):
    n = len(platform)
    m = len(platform[0])
    new_platform = []
    for i in range(m):
        new_platform.append([])
        for j in range(n):
            new_platform[i].append(platform[j][m - i - 1])
    return new_platform


def counter_rotate(platform):
    n = len(platform)
    m = len(platform[0])
    new_platform = []
    for i in range(m):
        new_platform.append([])
        for j in range(n):
            new_platform[i].append(platform[n - j - 1][i])
    return new_platform


def cycle(platform):
    return counter_rotate(north(counter_rotate(north(counter_rotate(north(counter_rotate(north(platform))))))))


def get_answer(start_of_cycle, cycle_length):
    target = 1000000000
    return start_of_cycle + ((target - start_of_cycle) % cycle_length)


def find_cycle(platform):
        seen = {}
        seen[get_hash(platform)] = 0
        platforms = [platform]

        for i in range(1000000000):
            platform = cycle(platform)
            platforms.append(platform)
            h = get_hash(platform)
            if h in seen:
                print("Cycle found after", i, "iterations. Cycle length is", i - seen[h])
                return i, i - seen[h], platforms[get_answer(seen[h], i - seen[h])]
            seen[h] = i
            if i > 0 and i % 100 == 0:
                print(i, "iterations done")

        return -1, -1, platform

def main():
    with open("14/input.txt") as f:
        platform = []
        for line in f:
            platform.append(line.strip())

        start_of_cycle, cycle_length, answer_platform = find_cycle(platform)
        print(eval(answer_platform))


if __name__ == '__main__':
    main()
