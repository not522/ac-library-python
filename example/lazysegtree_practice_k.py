# https://atcoder.jp/contests/practice2/tasks/practice2_k

import sys
from typing import Tuple

from atcoder.lazysegtree import LazySegTree
from atcoder.modint import ModContext, Modint


def main() -> None:
    with ModContext(998244353):
        n, q = map(int, sys.stdin.readline().split())
        a = [(Modint(ai), 1) for ai in map(int, sys.stdin.readline().split())]

        def op(x: Tuple[Modint, int],
               y: Tuple[Modint, int]) -> Tuple[Modint, int]:
            return x[0] + y[0], x[1] + y[1]

        e = Modint(0), 0

        def mapping(x: Tuple[Modint, Modint],
                    y: Tuple[Modint, int]) -> Tuple[Modint, int]:
            return x[0] * y[0] + x[1] * y[1], y[1]

        def composition(x: Tuple[Modint, Modint],
                        y: Tuple[Modint, Modint]) -> Tuple[Modint, Modint]:
            return x[0] * y[0], x[0] * y[1] + x[1]

        id_ = Modint(1), Modint(0)

        lazy_segtree = LazySegTree(op, e, mapping, composition, id_, a)

        for _ in range(q):
            t, *inputs = map(int, sys.stdin.readline().split())
            if t == 0:
                l, r, b, c = inputs
                lazy_segtree.apply(l, r, (Modint(b), Modint(c)))
            else:
                l, r = inputs
                print(lazy_segtree.prod(l, r)[0].val())


if __name__ == '__main__':
    main()
