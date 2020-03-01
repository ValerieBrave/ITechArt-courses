class RangeIterator:
    def __init__(self, size):
        self.c = 0
        self.first = 0
        self.second = 0
        self.third = 1
        self.size = size

    def __next__(self):
        self.c += 1
        if self.c > self.size:
            raise StopIteration
        if self.c == 1:
            return self.first
        if self.c == 2:
            return self.second
        if self.c == 3:
            return self.third
        new_trib = self.first + self.second + self.third
        self.first = self.second
        self.second = self.third
        self.third = new_trib
        return new_trib


class RangeIterable:
    def __init__(self, size):
        self.size = size

    def __iter__(self):
        return RangeIterator(self.size)


main_iter = RangeIterable(32)
for line in main_iter:
    print(line)
