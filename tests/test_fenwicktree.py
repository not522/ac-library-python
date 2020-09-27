import pytest
from typing import List, Tuple

from atcoder.fenwicktree import FenwickTree


@pytest.fixture
def fenwicktree() -> FenwickTree:
    return FenwickTree(5)


class TestFenwickTree:

    def test_initial_status(self, fenwicktree: FenwickTree) -> None:
        '''
        An initialized fenwicktree object is expected to have all the elements
        0.

        GIVEN an initialized fenwicktree object
        WHEN before executing fenwicktree.add(p, x)
        THEN all the elements are 0
        '''

        assert fenwicktree.data == [0, 0, 0, 0, 0]

        pair_of_positions = self._generate_pair_of_positions()

        for left, right in pair_of_positions:
            assert fenwicktree.sum(left, right) == 0

    def _generate_pair_of_positions(self) -> List[Tuple[int, ...]]:
        from itertools import combinations_with_replacement

        return list(combinations_with_replacement(range(5), 2))

    def test_add(self, fenwicktree: FenwickTree) -> None:
        '''
        fenwicktree.add(p, x) is expected to add x to the p-th of the number
        sequence.

        GIVEN an initialized fenwicktree object
        WHEN add 1 to the first in the number sequence
        THEN fenwicktree.data has [1, 1, 0, 1, 0]
        '''

        fenwicktree.add(0, 1)
        assert fenwicktree.data == [1, 1, 0, 1, 0]

    def test_add_multiple_times(self, fenwicktree: FenwickTree) -> None:
        '''
        fenwicktree.add(p, x) is expected to add x to the p-th of the number
        sequence.

        GIVEN an initialized fenwicktree object
        WHEN add arbitrary value(s) at arbitrary positions in the sequence
        THEN fenwicktree.data has a partial sum at any position in the sequence
        '''

        expected = [[1, 1, 0, 1, 0],
                    [1, 3, 0, 3, 0],
                    [1, 3, 3, 6, 0],
                    [1, 3, 3, 10, 0],
                    [1, 3, 3, 10, 5]
                    ]

        for i in range(5):
            fenwicktree.add(i, i + 1)
            assert fenwicktree.data == expected[i]

    def test_add_when_negative_value_is_given(
        self, fenwicktree: FenwickTree
    ) -> None:
        '''
        fenwicktree.add(p, x) is expected to add x to the p-th of the number
        sequence.

        GIVEN an initialized fenwicktree object
        WHEN add negative value at arbitrary positions in the sequence
        THEN fenwicktree.data has a partial sum at any position in the sequence
        '''

        for i in range(5):
            fenwicktree.add(i, i + 1)

        assert fenwicktree.data == [1, 3, 3, 10, 5]

        fenwicktree.add(0, -5)
        assert fenwicktree.data == [-4, -2, 3, 5, 5]

    def test_add_when_zero_is_given(self, fenwicktree: FenwickTree) -> None:
        '''
        fenwicktree.add(p, x) is expected to add x to the p-th of the number
        sequence.

        GIVEN an initialized fenwicktree object
        WHEN add zero at arbitrary positions in the sequence
        THEN fenwicktree.data has a partial sum at any position in the sequence
        '''

        for i in range(5):
            fenwicktree.add(i, i + 1)

        assert fenwicktree.data == [1, 3, 3, 10, 5]

        fenwicktree.add(0, 0)
        assert fenwicktree.data == [1, 3, 3, 10, 5]

    def test_add_when_positive_floating_point_value_is_given(
        self, fenwicktree: FenwickTree
    ) -> None:
        '''
        fenwicktree.add(p, x) is expected to add x to the p-th of the number
        sequence.

        GIVEN an initialized fenwicktree object
        WHEN add positive floating point value at arbitrary positions in the
             sequence
        THEN fenwicktree.data has a partial sum at any position in the sequence
        '''

        fenwicktree.add(0, 1.5)
        assert fenwicktree.data == [1.5, 1.5, 0, 1.5, 0]

    def test_add_when_negative_floating_point_value_is_given(
        self, fenwicktree: FenwickTree
    ) -> None:
        '''
        fenwicktree.add(p, x) is expected to add x to the p-th of the number
        sequence.

        GIVEN an initialized fenwicktree object
        WHEN add negative floating point value at arbitrary positions in the
             sequence
        THEN fenwicktree.data has a partial sum at any position in the sequence
        '''

        fenwicktree.add(0, -1.5)
        assert fenwicktree.data == [-1.5, -1.5, 0, -1.5, 0]

    @pytest.mark.parametrize((
        'left', 'right', 'expected'
    ), [
        (0, 5, 15),
        (0, 4, 10),
        (1, 4, 9),
        (1, 3, 5),
        (2, 2, 0),
    ])
    def test_sum(
        self, fenwicktree: FenwickTree, left: int, right: int, expected: int
    ) -> None:
        '''
        fenwicktree.sum(left, right) is expected to calculate the sum of the
        interval [left, right)

        GIVEN With arbitrary value(s) at arbitrary positions in the sequence
              added to an initialized fenwicktree object
        WHEN specify the interval [left, right)
        THEN returns the sum of interval [left, right)
        '''

        for i in range(5):
            fenwicktree.add(i, i + 1)

        assert fenwicktree.sum(left, right) == expected

    @pytest.mark.parametrize((
        'left', 'right', 'expected'
    ), [
        (0, 5, 17),
        (0, 4, 12),
        (0, 3, 8),
        (0, 2, 3),
        (0, 1, 1),
        (1, 4, 11),
        (1, 3, 7),
        (2, 2, 0),
    ])
    def test_sum_when_additional_element_is_given(
        self, fenwicktree: FenwickTree, left: int, right: int, expected: int
    ) -> None:
        '''
        fenwicktree.sum(left, right) is expected to calculate the sum of the
        interval [left, right)

        GIVEN With arbitrary value(s) at arbitrary positions in the sequence
              added to an initialized fenwicktree object
        WHEN specify the interval [left, right) after the additional element
             is given
        THEN returns the sum of interval [left, right)
        '''

        for i in range(5):
            fenwicktree.add(i, i + 1)

        assert fenwicktree.sum(0, 5) == 15

        fenwicktree.add(2, 2)
        assert fenwicktree.data == [1, 3, 5, 12, 5]
        assert fenwicktree.sum(left, right) == expected

    @pytest.mark.parametrize((
        'p'
    ), [
        -2,
        -1,
        5,
        6,
    ])
    def test_add_failed_if_invalid_input_is_given(
        self, fenwicktree: FenwickTree, p: int
    ) -> None:
        '''
        fenwicktree.add(p, x) is expected to be raised an AssertionError if an
        invalid input is given.

        GIVEN an initialized fenwicktree object
        WHEN an out-of-range index is given
        THEN raises an AssertionError
        '''

        with pytest.raises(AssertionError):
            fenwicktree.add(p, None)

    @pytest.mark.parametrize((
        'left', 'right'
    ), [
        (-2, 5),
        (-1, 5),
        (0, 6),
        (0, 7),
        (3, 2),
        (-1, 6),
        (-1, 7),
    ])
    def test_sum_failed_if_invalid_input_is_given(
        self, fenwicktree: FenwickTree, left: int, right: int
    ) -> None:
        '''
        fenwicktree.sum(left, right) is expected to be raised an AssertionError
        if an invalid input is given.

        GIVEN an initialized fenwicktree object
        WHEN an out-of-range index is given
        THEN raises an AssertionError
        '''

        with pytest.raises(AssertionError):
            fenwicktree.sum(left, right)
