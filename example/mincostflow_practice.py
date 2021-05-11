# https://atcoder.jp/contests/practice2/tasks/practice2_e

import sys
from typing import List

from atcoder.mincostflow import MCFGraph


def main() -> None:
    n, k = map(int, sys.stdin.readline().split())
    s = n * 2
    t = s + 1
    g = MCFGraph(t + 1)
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    big = 10 ** 9
    edges: List[List[int]] = list([] for _ in range(n))
    for i in range(n):
        g.add_edge(s, i, k, 0)
        g.add_edge(i + n, t, k, 0)
        for j in range(n):
            edges[i].append(g.add_edge(i, j + n, 1, big - grid[i][j]))
    g.add_edge(s, t, n * k, big)

    cost = g.flow(s, t, n * k)[1]
    print(big * n * k - cost)

    result = list(['.'] * n for _ in range(n))
    for i in range(n):
        for j in range(n):
            if g.get_edge(edges[i][j]).flow > 0:
                result[i][j] = 'X'

    for r in result:
        print("".join(r))


if __name__ == '__main__':
    main()
