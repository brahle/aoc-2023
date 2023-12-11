
res = 0

with open("/Users/brahle/dev/github/brahle/aoc-2023/01/input_part_1.txt") as f:
    for line in f:
        start = None
        end = None
        for char in line:
            if '0' <= char <= '9':
                if start is None:
                    start = char
                end = char
        res += int(f"{start}{end}")

print(res)
