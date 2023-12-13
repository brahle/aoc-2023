

class Counter:
    def __init__(self, record, parts):
        self.record = record
        self.parts = parts
        self.n = len(record)
        self.m = len(parts)
        self.dp = [[None for _ in range(self.m + 1)] for __ in range(self.n)]

    def count(self):
        return self._count(0, 0)

    def _count(self, i, j):
        # print("count", i, j, "->", self.record[i:], self.parts[j:])

        if i >= self.n:
            return 1 if j == self.m else 0

        if i > self.n:
            return 0

        if self.dp[i][j] is not None:
            return self.dp[i][j]

        if self.record[i] == ".":
            res = self._count(i + 1, j)
        elif self.record[i] == "#":
            if j == self.m or not self.can_start_group_at(i, j):
                return 0
            res = self._count(i + self.parts[j] + 1, j + 1)
        else:
            # print("At position", i, "we have", self.record[i], f"and can start group is {self.can_start_group_at(i, j)}")
            res = self._count(i + 1, j)
            if j < self.m and self.can_start_group_at(i, j):
                # print("Calling recurisvely from", i, j, "to", i + self.parts[j] + 1, j + 1)
                res += self._count(i + self.parts[j] + 1, j + 1)
        self.dp[i][j] = res
        return res

    def can_start_group_at(self, i, j):
        if j >= self.m or i + self.parts[j] > self.n:
            return False
        for k in range(self.parts[j]):
            if self.record[i + k] == ".":
                return False
        if i + self.parts[j] < self.n and self.record[i + self.parts[j]] == "#":
            return False
        return True


def main():
    with open("12/input.txt") as f:
        total = 0
        for line in f:
            record, groups = line.split()
            values = [int(x) for x in groups.split(",")]
            record = "?".join([record for _ in range(5)])
            values = values * 5

            counter = Counter(record, values)
            res = counter.count()
            print(record, values, res)
            total += res
            # break
        print(total)

if __name__ == '__main__':
    main()
