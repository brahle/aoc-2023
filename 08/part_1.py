from re import compile


regex = compile(r'(?P<node>\w+) = \((?P<left>\w+), (?P<right>\w+)\)')


def main():
    sides = {}

    with open('08/input.txt') as f:
        sequence = f.readline().strip()
        _ = f.readline()

        for line in f:
            match = regex.match(line)
            node = match.group('node')
            left = match.group('left')
            right = match.group('right')
            sides[node] = {
                'L': left,
                'R': right,
            }

        current = 'AAA'
        steps = 0
        n = len(sequence)
        while current != 'ZZZ':
            current = sides[current][sequence[steps % n]]
            steps += 1
    print(steps)


if __name__ == '__main__':
    main()
