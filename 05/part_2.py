import re
from enum import Enum

regex = re.compile(r"(?P<source>.*)-to-(?P<destination>.*) map:")
seeds_regex = re.compile(r"seeds: (\d| )+")


class EventType(Enum):
    SEED_END = 0
    RANGE_END = 1
    RANGE_START = 2
    SEED_START = 3


class Event():
    def __init__(self, time, event_type, destination=None):
        self.time = time
        self.event_type = event_type
        self.destination = destination

    def __lt__(self, other):
        if self.time != other.time:
            return self.time < other.time
        return self.event_type.value < other.event_type.value

    def __repr__(self):
        return f"Event({self.time}, {self.event_type}, {self.destination})"


class SeedRange():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start}, {self.end}>"

    def __lt__(self, other):
        return self.start < other.start


def transform(events, seeds):
    for seed in seeds:
        events.append(Event(seed.start, EventType.SEED_START))
        events.append(Event(seed.end, EventType.SEED_END))

    events.sort()
    current_translation = 0
    seed_start = None
    new_seeds = []

    for event in events:
        print(event, seed_start, current_translation)
        if event.event_type == EventType.SEED_START:
            seed_start = event.time

        elif event.event_type == EventType.RANGE_START:
            if seed_start is not None and seed_start < event.time:
                new_seeds.append(SeedRange(seed_start + current_translation, event.time + current_translation))
                seed_start = event.time
            current_translation = event.destination - event.time

        elif event.event_type == EventType.RANGE_END:
            if seed_start is not None and seed_start < event.time:
                new_seeds.append(SeedRange(seed_start + current_translation, event.time + current_translation))
                seed_start = event.time
            current_translation = 0

        elif event.event_type == EventType.SEED_END:
            if seed_start < event.time:
                new_seeds.append(SeedRange(seed_start + current_translation, event.time + current_translation))
            seed_start = None

    return new_seeds


def main():
    with open("05/input.txt") as f:

        events = None
        seeds = []
        cnt = 0

        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith("seeds: "):
                seed_pairs = [int(x) for x in line.split()[1:]]
                for i in range(len(seed_pairs) // 2):
                    seed = seed_pairs[i * 2]
                    count = seed_pairs[i * 2 + 1]
                    seeds.append(SeedRange(seed, seed + count))
                print(seeds)
                continue

            match = regex.match(line)
            if match:
                if events:
                    seeds = transform(events, seeds)
                    print(seeds)
                events = []
                continue

            destination_start, source_start, range_length = [int(x) for x in line.split()]
            events.append(Event(source_start, EventType.RANGE_START, destination_start))
            events.append(Event(source_start + range_length, EventType.RANGE_END))


    seeds = transform(events, seeds)
    print(min(seeds))

if __name__ == '__main__':
    main()
