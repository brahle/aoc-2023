from math import ceil, floor


def parse(line):
    variable_name, values = line.split(":")
    return [int(x) for x in values.split()]


def solve(t, d):
    a = 1
    b = -t
    c = d

    mini = (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a) + 1e-9
    maxi = (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a) - 1e-9

    diff = floor(maxi) - ceil(mini) + 1
    return mini, maxi, diff


def main():
    with open("06/input_2.txt", "r") as f:
        times = parse(f.readline())
        print(times)
        distances = parse(f.readline())
        print(distances)

        n = len(times)

        res = 1
        for i in range(n):
            res *= solve(times[i], distances[i])[2]
            print(times[i], distances[i], solve(times[i], distances[i]))
        print(res)


if __name__ == "__main__":
    main()
