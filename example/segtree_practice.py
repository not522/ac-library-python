# https://atcoder.jp/contests/practice2/tasks/practice2_j

import sys

from atcoder.segtree import SegTree


def main() -> None:
    n, q = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    segtree = SegTree(max, -1, a)

    for _ in range(q):
        t, x, y = map(int, sys.stdin.readline().split())
        if t == 1:
            segtree.set(x - 1, y)
        elif t == 2:
            print(segtree.prod(x - 1, y))
        else:
            print(segtree.max_right(x - 1, lambda v: v < y) + 1)


if __name__ == '__main__':
    main()
