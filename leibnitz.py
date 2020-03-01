import math


class RangeIterator:
    def __init__(self):
        self.c = 0
        self.x = 1
        self.sum = 0
        self.max = round((math.pi / 4), 2)

    def __next__(self):
        if self.sum > self.max and self.sum != 1:
            raise StopIteration
        if self.c == 0:
            self.c += 1
            self.sum += round(self.x, 2)
            return self.x
        else:
            self.x = round((math.pow(-1, self.c)) / (2 * self.c + 1), 2)
            self.c += 1
            self.sum += round(self.x, 2)
            return self.x


class RangeIterable:
    def __iter__(self):
        return RangeIterator()


main_iter = RangeIterable()
for line in main_iter:
    print(line)
