# https://atcoder.jp/contests/practice2/tasks/practice2_b

import sys

from atcoder.scc import SCCGraph


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    g = SCCGraph(n)

    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        g.add_edge(u, v)

    scc = g.scc()

    print(len(scc))
    for v in scc:
        print(len(v), end='')
        for x in v:
            print(f' {x}', end='')
        print('')


if __name__ == '__main__':
    main()
