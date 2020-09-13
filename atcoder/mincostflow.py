from __future__ import annotations

from typing import NamedTuple, Optional, List
from heapq import heappush, heappop


class MCFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int
        cost: int

    class _Edge:
        def __init__(self, dst: int, cap: int, cost: int) -> None:
            self.dst = dst
            self.cap = cap
            self.cost = cost
            self.rev: Optional[MCFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MCFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MCFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int, cost: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MCFGraph._Edge(dst, cap, cost)
        re = MCFGraph._Edge(src, 0, -cost)
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
        return MCFGraph.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap,
            e.cost
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> (int, int):
        return self.slope(s, t, flow_limit)[-1]

    def slope(self, s: int, t: int, flow_limit: Optional[int] = None) -> List[(int, int)]:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = sum(e.cap for e in self._g[s])

        dual = [0] * self._n
        prev: List[Optional[(int, MCFGraph._Edge)]] = [None] * self._n

        def refine_dual() -> bool:
            pq = [(0, s)]
            visited = [False] * self._n
            dist: List[Optional[int]] = [None] * self._n
            dist[s] = 0
            while pq:
                (dist_v, v) = heappop(pq)
                if visited[v]:
                    continue
                visited[v] = True
                if v == t:
                    break
                dual_v = dual[v]
                for e in self._g[v]:
                    w = e.dst
                    if visited[w] or e.cap == 0:
                        continue
                    reduced_cost = e.cost - dual[w] + dual_v
                    new_dist = dist_v + reduced_cost
                    dist_w = dist[w]
                    if dist_w is None or new_dist < dist_w:
                        dist[w] = new_dist
                        prev[w] = (v, e)
                        heappush(pq, (new_dist, w))
            else:
                return False
            dist_t = dist[t]
            for v in range(self._n):
                if visited[v]:
                    dual[v] -= dist_t - dist[v]
            return True

        flow = 0
        cost = 0
        prev_cost_per_flow: Optional[int] = None
        result = [(flow, cost)]
        while flow < flow_limit:
            if not refine_dual():
                break
            f = flow_limit - flow
            v = t
            while prev[v] is not None:
                (u, e) = prev[v]
                f = min(f, e.cap)
                v = u
            v = t
            while prev[v] is not None:
                (u, e) = prev[v]
                e.cap -= f
                e.rev.cap += f
                v = u
            c = -dual[s]
            flow += f
            cost += f * c
            if c == prev_cost_per_flow:
                result.pop()
            result.append((flow, cost))
            prev_cost_per_flow = c
        return result


# https://atcoder.jp/contests/practice2/tasks/practice2_e
def main() -> None:
    import sys
    n, k = map(int, sys.stdin.readline().split())
    s = n * 2
    t = s + 1
    g = MCFGraph(t + 1)
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    big = 10 ** 9
    edges = list([] for _ in range(n))
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

    for s in result:
        print("".join(s))


if __name__ == '__main__':
    main()
