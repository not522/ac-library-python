import random

from atcoder.dsu import DSU


class DSUSuite:

    def setup(self) -> None:
        random.seed(0)
        self.n = 100000
        self.pairs = []
        for _ in range(1000000):
            a = random.randrange(0, self.n)
            b = random.randrange(0, self.n)
            self.pairs.append((a, b))

    def time_dsu_merge(self) -> None:
        dsu = DSU(self.n)
        for i, j in self.pairs:
            dsu.merge(i, j)
