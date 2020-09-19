# https://atcoder.jp/contests/practice2/tasks/practice2_b

import sys

from atcoder.fenwicktree import FenwickTree


def main() -> None:
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
