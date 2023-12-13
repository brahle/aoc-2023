from re import compile


regex = compile(r'(?P<node>\w+) = \((?P<left>\w+), (?P<right>\w+)\)')


def done(current):
    return all((x.endswith('Z') for x in current))


def find_cycle(start, sequence, sides):
    current = start
    steps = 0
    n = len(sequence)
    visited = {
        node: [-1 for i in range(n)] for node in sides.keys()
    }

    ends_with_z = []

    while visited[current][steps % n] == -1:
        visited[current][steps % n] = steps
        if current.endswith('Z'):
            ends_with_z.append(steps)
        current = sides[current][sequence[steps % n]]
        steps += 1

    return visited[current][steps % n], steps - visited[current][steps % n], ends_with_z


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    return all((n % i for i in range(2, n)))


def lcm(numbers):
    lcm_result = 1
    for num in numbers:
        lcm_result = lcm_result * num // gcd(lcm_result, num)
    return lcm_result


def main():
    sides = {}

    with open('08/input.txt') as f:
        sequence = f.readline().strip()
        _ = f.readline()

        current = []

        for line in f:
            match = regex.match(line)
            node = match.group('node')
            left = match.group('left')
            right = match.group('right')
            sides[node] = {
                'L': left,
                'R': right,
            }
            if node.endswith('A'):
                current.append(node)

        cycles = [
            find_cycle(start, sequence, sides) for start in current
        ]

        for cycle in cycles:
            print(cycle)

        # I got lucky and this works for my input :)
        result = lcm([cycle[1] for cycle in cycles])
        print(result)

if __name__ == '__main__':
    main()

