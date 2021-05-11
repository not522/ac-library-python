# https://atcoder.jp/contests/practice2/tasks/practice2_d

import sys
from typing import Tuple

from atcoder.maxflow import MFGraph


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    s = n * m
    t = s + 1
    g = MFGraph(t + 1)
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

    def enc(i: int, j: int) -> int:
        return i * m + j

    def dec(v: int) -> Tuple[int, int]:
        return v // m, v % m

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                continue
            if (i + j) % 2 == 0:
                g.add_edge(s, enc(i, j), 1)
            else:
                g.add_edge(enc(i, j), t, 1)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 1 or grid[i][j] == '#':
                continue
            for direction in range(4):
                ii = i + dx[direction]
                jj = j + dy[direction]
                if 0 <= ii < n and 0 <= jj < m and grid[ii][jj] == '.':
                    g.add_edge(enc(i, j), enc(ii, jj), 1)

    print(g.flow(s, t))
    for e in g.edges():
        if e.src == s or e.dst == t or e.flow == 0:
            continue
        (i, j) = dec(e.src)
        (ii, jj) = dec(e.dst)
        if i == ii + 1:
            grid[ii][jj] = 'v'
            grid[i][j] = '^'
        elif j == jj + 1:
            grid[ii][jj] = '>'
            grid[i][j] = '<'
        elif i == ii - 1:
            grid[i][j] = 'v'
            grid[ii][jj] = '^'
        else:
            grid[i][j] = '>'
            grid[ii][jj] = '<'

    for r in grid:
        print("".join(r))


if __name__ == '__main__':
    main()
