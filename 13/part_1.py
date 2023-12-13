
def check_horizontal(pattern, x):
    max_range = min(x, len(pattern) - x)
    for i in range(max_range):
        if pattern[x - i - 1] != pattern[x + i]:
            return False
    return True


def check_vertical(pattern, x):
    max_range = min(x, len(pattern[0]) - x)
    for i in range(max_range):
        for k in range(len(pattern)):
            if pattern[k][x - i - 1] != pattern[k][x + i]:
                return False
    return True


def find_mirror(pattern):
    for i in range(1, len(pattern)):
        if check_horizontal(pattern, i):
            return i * 100

    for j in range(1, len(pattern[0])):
        if check_vertical(pattern, j):
            return j

    assert False, "No mirror found"

def main():
    with open("13/input.txt") as f:
        pattern = []
        res = 0
        for line in f:
            line = line.strip()
            if line == "":
                res += find_mirror(pattern)
                pattern = []
            else:
                pattern.append(line)
        if pattern:
            res += find_mirror(pattern)
        print(res)


if __name__ == '__main__':
    main()
