# https://atcoder.jp/contests/practice2/tasks/practice2_l

import sys
from typing import Tuple

from atcoder.lazysegtree import LazySegTree


def main() -> None:
    n, q = map(int, sys.stdin.readline().split())
    a = []
    for x in map(int, sys.stdin.readline().split()):
        if x == 0:
            a.append((1, 0, 0))
        else:
            a.append((0, 1, 0))

    def op(x: Tuple[int, int, int],
           y: Tuple[int, int, int]) -> Tuple[int, int, int]:
        return x[0] + y[0], x[1] + y[1], x[2] + y[2] + x[1] * y[0]

    e = (0, 0, 0)

    def mapping(x: bool, y: Tuple[int, int, int]) -> Tuple[int, int, int]:
        if not x:
            return y
        return y[1], y[0], y[0] * y[1] - y[2]

    def composition(x: bool, y: bool) -> bool:
        return (x and not y) or (not x and y)

    id_ = False

    lazy_segtree = LazySegTree(op, e, mapping, composition, id_, a)
    for _ in range(q):
        t, left, right = map(int, sys.stdin.readline().split())
        left -= 1
        if t == 1:
            lazy_segtree.apply(left, right, True)
        else:
            print(lazy_segtree.prod(left, right)[2])


if __name__ == '__main__':
    main()
