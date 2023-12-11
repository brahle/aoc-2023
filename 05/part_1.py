import re

regex = re.compile(r"(?P<source>.*)-to-(?P<destination>.*) map:")
seeds_regex = re.compile(r"seeds: (\d| )+")


class RangeTranslation():
    def __init__(self, destination_start, source_start, range_length):
        self.start = source_start
        self.end = source_start + range_length
        self.destination = destination_start

    def contains(self, value):
        return self.start <= value < self.end

    def convert(self, value):
        return value - self.start + self.destination


def transform(current_map, seeds):
    print(current_map)
    print(seeds)
    new_seeds = []
    for seed in seeds:
        for translation in current_map:
            if translation.contains(seed):
                new_seeds.append(translation.convert(seed))
                break
        else:
            new_seeds.append(seed)
    print(new_seeds)
    return new_seeds


def main():
    with open("05/input.txt") as f:

        current_map = None
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith("seeds: "):
                seeds = list(sorted([int(x) for x in line.split()[1:]]))
                continue

            match = regex.match(line)
            if match:
                if current_map:
                    seeds = transform(current_map, seeds)
                current_map = []
                continue

            current_map.append(RangeTranslation(*[int(x) for x in line.split()]))

    seeds = transform(current_map, seeds)
    print(min(seeds))

if __name__ == '__main__':
    main()
