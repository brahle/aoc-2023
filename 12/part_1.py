def verify(values, record):
    record_values = []
    current = 0
    for i in range(len(record)):
        if record[i] == "#":
            current += 1
        else:
            if current > 0:
                record_values.append(current)
            current = 0
    if current > 0:
        record_values.append(current)
    return record_values == values

def check(record, values, current=None, i=0):
    if current is None:
        current = ""
    if i == len(record):
        return 1 if verify(values, current) else 0
    if record[i] == "?":
        return (
            check(record, values, current + "#", i + 1) +
            check(record, values, current + ".", i + 1)
        )
    else:
        return check(record, values, current + record[i], i + 1)


def main():
    with open("12/input.txt") as f:
        total = 0
        for line in f:
            record, groups = line.split()
            values = [int(x) for x in groups.split(",")]
            res = check(record, values)
            print(record, values, res)
            total += res
        print(total)

if __name__ == '__main__':
    main()
