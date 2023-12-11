values = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def isdigit(x):
    return '0' <= x <= '9'


def check(line):
    if isdigit(line[0]):
        return int(line[0])
    for word, value in values.items():
        if line.startswith(word):
            return value
    return None


def process(line):
    start = None
    end = None
    for i in range(len(line)):
        val = check(line[i:])
        if val is not None:
            if start is None:
                start = val
            end = val
    return start * 10 + end


res = 0
with open("/Users/brahle/dev/github/brahle/aoc-2023/01/input_part_1.txt") as f:
    for line in f:
        res += process(line)
print(res)
