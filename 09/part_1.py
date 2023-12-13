
def solve(numbers):
    if all([x == 0 for x in numbers]):
        return 0
    new_numbers = []
    prev = numbers[0]
    for i in range(1, len(numbers)):
        new_numbers.append(numbers[i] - prev)
        prev = numbers[i]
    return numbers[-1] + solve(new_numbers)


def main():
    with open("09/input.txt") as f:
        result = 0
        for line in f:
            result += solve([int(x) for x in line.strip().split()])
    print(result)

if __name__ == '__main__':
    main()
