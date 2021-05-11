# https://atcoder.jp/contests/practice2/tasks/practice2_k

import sys
from typing import Tuple

from atcoder.lazysegtree import LazySegTree


def main() -> None:
    mod = 998244353

    n, q = map(int, sys.stdin.readline().split())
    a = [(ai, 1) for ai in map(int, sys.stdin.readline().split())]

    def op(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple[int, int]:
        return (x[0] + y[0]) % mod, x[1] + y[1]

    e = 0, 0

    def mapping(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple[int, int]:
        return (x[0] * y[0] + x[1] * y[1]) % mod, y[1]

    def composition(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple[int, int]:
        return (x[0] * y[0]) % mod, (x[0] * y[1] + x[1]) % mod

    id_ = 1, 0

    lazy_segtree = LazySegTree(op, e, mapping, composition, id_, a)

    for _ in range(q):
        t, *inputs = map(int, sys.stdin.readline().split())
        if t == 0:
            l, r, b, c = inputs
            lazy_segtree.apply(l, r, (b, c))
        else:
            l, r = inputs
            print(lazy_segtree.prod(l, r)[0])


if __name__ == '__main__':
    main()
