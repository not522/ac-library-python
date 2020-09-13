from __future__ import annotations

from typing import NamedTuple, Optional, List


class MaxFlow:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int):
            self.dst = dst
            self.cap = cap
            self.rev: Optional[MaxFlow._Edge] = None

    def __init__(self, n: int):
        self._n = n
        self._g: List[List[MaxFlow._Edge]] = [[] for _ in range(n)]
        self._edges: List[MaxFlow._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MaxFlow._Edge(dst, cap)
        re = MaxFlow._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = e.rev
        return MaxFlow.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int):
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = sum(e.cap for e in self._g[s])

        current_edge = [0] * self._n
        level = [0] * self._n

        def fill(arr: List[int], value: int):
            for i in range(len(arr)):
                arr[i] = value

        def bfs() -> bool:
            fill(level, self._n)
            queue = []
            q_front = 0
            queue.append(s)
            level[s] = 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim) -> int:
            stack = []
            edge_stack = []
            stack.append(t)
            while stack:
                v = stack[-1]
                if v == s:
                    flow = min(lim, min(edge_stack, key=lambda e: e.cap))
                    for e in edge_stack:
                        e.cap -= flow
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = e.rev
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    stack.append(e.dst)
                    edge_stack.append(re)
                    break
                else:
                    stack.pop()
                    if edge_stack:
                        edge_stack.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            fill(current_edge, 0)
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> List[bool]:
        visited = [False] * self._n
        stack = [s]
        visited[s] = True
        while stack:
            v = stack.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    stack.append(e.dst)
        return visited


# https://atcoder.jp/contests/practice2/tasks/practice2_d
def main() -> None:
    import sys
    n, m = map(int, sys.stdin.readline().split())
    s = n * m
    t = s + 1
    g = MaxFlow(t + 1)
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

    def enc(i: int, j: int) -> int:
        return i * m + j

    def dec(v: int) -> (int, int):
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

    for s in grid:
        print("".join(s))


if __name__ == '__main__':
    main()
