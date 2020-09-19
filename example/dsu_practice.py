# https://atcoder.jp/contests/practice2/tasks/practice2_a

import sys

from atcoder.dsu import DSU


def main() -> None:
    n, q = map(int, sys.stdin.readline().split())
    dsu = DSU(n)

    for _ in range(q):
        t, u, v = map(int, sys.stdin.readline().split())
        if t == 0:
            dsu.merge(u, v)
        if t == 1:
            if dsu.same(u, v):
                print(1)
            else:
                print(0)


if __name__ == '__main__':
    main()
