import typing

import atcoder._scc


class SCCGraph:
    def __init__(self, n: int = 0) -> None:
        self._internal = atcoder._scc.SCCGraph(n)

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        n = self._internal.num_vertices()
        assert 0 <= from_vertex < n
        assert 0 <= to_vertex < n
        self._internal.add_edge(from_vertex, to_vertex)

    def scc(self) -> typing.List[typing.List[int]]:
        return self._internal.scc()
