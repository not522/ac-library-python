import typing

import atcoder._scc


class TwoSAT:
    '''
    2-SAT

    Reference:
    B. Aspvall, M. Plass, and R. Tarjan,
    A Linear-Time Algorithm for Testing the Truth of Certain Quantified Boolean
    Formulas
    '''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self._answer = [False] * n
        self._scc = atcoder._scc.SCCGraph(2 * n)

    def add_clause(self, i: int, f: bool, j: int, g: bool) -> None:
        assert 0 <= i < self._n
        assert 0 <= j < self._n

        self._scc.add_edge(2 * i + (0 if f else 1), 2 * j + (1 if g else 0))
        self._scc.add_edge(2 * j + (0 if g else 1), 2 * i + (1 if f else 0))

    def satisfiable(self) -> bool:
        scc_id = self._scc.scc_ids()[1]
        for i in range(self._n):
            if scc_id[2 * i] == scc_id[2 * i + 1]:
                return False
            self._answer[i] = scc_id[2 * i] < scc_id[2 * i + 1]
        return True

    def answer(self) -> typing.List[bool]:
        return self._answer
