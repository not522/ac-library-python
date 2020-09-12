import typing


class FenwickTree:
    '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


# https://atcoder.jp/contests/practice2/tasks/practice2_b
def main() -> None:
    import sys

    n, q = map(int, sys.stdin.readline().split())
    fenwick_tree = FenwickTree(n)

    a = map(int, sys.stdin.readline().split())
    for i, ai in enumerate(a):
        fenwick_tree.add(i, ai)

    for _ in range(q):
        t, x, y = map(int, sys.stdin.readline().split())
        if t == 0:
            fenwick_tree.add(x, y)
        if t == 1:
            print(fenwick_tree.sum(x, y))


if __name__ == '__main__':
    main()
