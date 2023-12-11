
def score(line):
    card_id, numbers = line.split(":")
    winning, my = numbers.split("|")

    winning = set(winning.split())
    my = set(my.split())
    overlaps = len(winning.intersection(my))
    return overlaps



def main():
    res = 0
    copies = [1 for i in range(1000)]

    with open("04/input.txt") as f:
        for i, line in enumerate(f):
            res += copies[i]
            for j in range(i + 1, i + score(line) + 1):
                copies[j] += copies[i]

    print(res)

if __name__ == '__main__':
    main()
