from itertools import combinations
import pytest
import random
from typing import List, Tuple

from atcoder.dsu import DSU


class TestDsu:

    def test_initial_status(self) -> None:
        dsu = DSU(5)

        for i, j in combinations(range(5), 2):
            assert not dsu.same(i, j)

        for index in range(5):
            assert dsu.size(index) == 1
            assert dsu.leader(index) == index

        assert dsu.groups() == [[0], [1], [2], [3], [4]]

    def test_merge(self) -> None:
        dsu = DSU(5)

        assert not dsu.same(0, 1)

        dsu.merge(0, 1)
        assert dsu.same(0, 1)

        # Test assertion of invalid pairs
        for i in range(-1, 6):
            for j in range(-1, 6):
                if not (0 <= i < 5 and 0 <= j < 5):
                    with pytest.raises(AssertionError):
                        dsu.merge(i, j)

    def test_merge_elements_of_same_group(self) -> None:
        dsu = DSU(5)

        assert not dsu.same(0, 1)

        for _ in range(2):
            dsu.merge(0, 1)
            assert dsu.same(0, 1)

        # Test assertion of invalid pairs
        for i in range(-1, 6):
            for j in range(-1, 6):
                if not (0 <= i < 5 and 0 <= j < 5):
                    with pytest.raises(AssertionError):
                        dsu.same(i, j)

    def test_size(self) -> None:
        dsu = DSU(5)

        dsu.merge(0, 1)
        assert dsu.size(0) == 2
        dsu.merge(0, 2)
        assert dsu.size(0) == 3

        # Test assertion of invalid indices
        for i in (-1, 5):
            with pytest.raises(AssertionError):
                dsu.size(i)

    def test_leader(self) -> None:
        dsu = DSU(5)

        dsu.merge(0, 1)
        dsu.merge(0, 2)

        assert dsu.leader(1) in [0, 1, 2]
        assert dsu.leader(2) in [0, 1, 2]
        assert dsu.leader(1) == dsu.leader(2)
        assert dsu.leader(3) not in [0, 1, 2]
        assert dsu.leader(4) not in [0, 1, 2]

        # Test assertion of invalid indices
        for i in (-1, 5):
            with pytest.raises(AssertionError):
                dsu.leader(i)

    def test_groups(self) -> None:
        dsu = DSU(5)

        dsu.merge(0, 1)
        dsu.merge(0, 2)

        assert dsu.groups() == [[0, 1, 2], [3], [4]]
