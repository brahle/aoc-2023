
def score(line):
    card_id, numbers = line.split(":")
    winning, my = numbers.split("|")

    winning = set(winning.split())
    my = set(my.split())
    overlaps = len(winning.intersection(my))
    if overlaps == 0:
        return 0
    return 2 ** (overlaps - 1)



def main():
    res = 0
    with open("04/input.txt") as f:
        for line in f:
            res += score(line)
    print(res)

if __name__ == '__main__':
    main()
