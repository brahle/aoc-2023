
LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def process(line):
    left, right = line.split(":")
    game_id = int(left.split()[1])

    games = right.split(";")
    for game in games:
        parts = game.split(",")
        for part in parts:
            count, color = part.split()
            count = int(count)
            if LIMITS[color] < count:
                return 0

    return game_id



def main():
    with open("02/input.txt") as f:
        res = 0
        for line in f:
            res += process(line)

    print(res)


if __name__ == '__main__':
    main()
