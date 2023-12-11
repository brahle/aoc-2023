

def process(line):
    left, right = line.split(":")
    game_id = int(left.split()[1])
    games = right.split(";")
    min_count = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for game in games:
        parts = game.split(",")
        for part in parts:
            count, color = part.split()
            count = int(count)
            if min_count[color] < count:
                min_count[color] = count

    return min_count["red"] * min_count["blue"] * min_count["green"]



def main():
    with open("02/input.txt") as f:
        res = 0
        for line in f:
            res += process(line)

    print(res)


if __name__ == '__main__':
    main()
