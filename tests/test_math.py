import pytest
from typing import List, Tuple

from atcoder.math import inv_mod, crt, floor_sum


class TestMath:

    def test_inv_mod(self) -> None:
        '''
        inv_mod(a, b) is expected to returns an integer y such that 0 <= y < m
        and xy ≡ 1 (mod m).

        GIVEN parameters a and b (>= 1), gcd(a, b) = 1
        WHEN inv_mod(a, b) is called
        THEN return an integer y such that 0 <= y < m and xy ≡ 1 (mod m)
        '''

        from math import gcd

        for a in range(-100, 100 + 1):
            for b in range(1, 1000 + 1):
                if gcd(a % b, b) != 1:
                    continue

                c = inv_mod(a, b)
                assert 0 <= c < b
                assert 1 % b == (((a * c) % b + b) % b)

    def test_inv_mod_when_returns_zero(self) -> None:
        '''
        inv_mod(a, b) is expected to returns an integer y such that 0 <= y < m
        and xy ≡ 1 (mod m).

        GIVEN parameters a and b (= 1), gcd(a, b) = 1
        WHEN inv_mod(a, b) is called
        THEN return 0
        '''

        assert inv_mod(0, 1) == 0

        for i in range(10):
            assert inv_mod(i, 1) == 0
            assert inv_mod(-i, 1) == 0

    @pytest.mark.parametrize((
        'r', 'm',
        'expected'
    ), [
        ([44, 23, 13], [13, 50, 22],
         (1773, 7150)
         ),
        ([12345, 67890, 99999], [13, 444321, 95318],
         (103333581255, 550573258014)
         ),
        ([0, 3, 4], [1, 9, 5],
         (39, 45)
         ),
        ([1, 2, 1], [2, 3, 2],
         (5, 6)
         ),
        ([], [],
         (0, 1)
         ),
    ])
    def test_crt(
        self, r: List[int], m: List[int], expected: Tuple[int, int]
    ) -> None:
        '''
        crt(r, m) is expected to return a pair of tuple value.

        GIVEN two arrays of the same size
        WHEN crt(r, m) is called
        THEN return a pair of tuple value.
        '''

        assert crt(r, m) == expected

    def test_floor_sum(self) -> None:
        '''
        floor_sum(n, m, a, b) is expected to return Σfloor((a * i + b) // m).

        GIVEN parameter n(>= 1), m(>= 1), a, b
        WHEN floor_sum(n, m, a, b) and self._floor_sum_naive(n, m, a, b) are
             called
        THEN the return values of the two methods match
        '''

        value_max = 20

        for n in range(1, value_max + 1):
            for m in range(1, value_max + 1):
                for a in range(value_max + 1):
                    for b in range(value_max + 1):
                        assert floor_sum(n, m, a, b) \
                            == self._floor_sum_naive(n, m, a, b)

    def _floor_sum_naive(self, n: int, m: int, a: int, b: int) -> int:
        total = 0

        for i in range(n):
            total += (a * i + b) // m

        return total

    @pytest.mark.parametrize((
        'n', 'm', 'a', 'b', 'expected'
    ), [
        (4, 10, 6, 3, 3),
        (6, 5, 4, 3, 13),
        (1, 1, 0, 0, 0),
        (31415, 92653, 58979, 32384, 314_095_480),
        (1000000000, 1000000000, 999999999, 999999999, 499999999500000000),
    ])
    def test_floor_sum_using_acl_practice_contest(
        self, n: int, m: int, a: int, b: int, expected: int
    ) -> None:
        '''
        Run floor_sum(n, m, a, b) using samples of ACL Practice Contest

        See:
        https://atcoder.jp/contests/practice2/tasks/practice2_c
        '''
        assert floor_sum(n, m, a, b) == expected

    @pytest.mark.parametrize((
        'a', 'b'
    ), [
        (2, -1),
        (2, 0),
        (271828, 0),
        (6, 3),
        (3, 6),
        (3141592, 1000000008),
    ])
    def test_inv_mod_failed_if_invalid_input_is_given(
        self, a: int, b: int
    ) -> None:
        '''
        inv_mod(a, b) is expected to be raised an AssertionError if an
        invalid input is given.

        GIVEN parameter a, b(< 1) or gcd(a, b) != 1
        WHEN inv_mod(a, b) is called
        THEN raises an AssertionError
        '''

        with pytest.raises(AssertionError):
            inv_mod(a, b)

    @pytest.mark.parametrize((
        'r', 'm',
    ), [
        ([], [1, 2]),
        ([1, 2], []),
        ([3], [1, 2]),
        ([1, 2], [1]),
        ([1, 2], [0, 0]),
        ([1, 2], [1, 0]),
        ([1, 2], [0, 1]),
        ([1, 2], [1, -1]),
        ([1, 2], [-1, -1]),
    ])
    def test_crt_failed_if_invalid_input_is_given(
        self, r: List[int], m: List[int]
    ) -> None:
        '''
        crt(r, m) is expected to be raised an AssertionError if an invalid
        input is given.

        GIVEN two arrays of different sizes or
              any one of m is less than or equal to zero
        WHEN crt(r, m) is called
        THEN raises an AssertionError
        '''

        with pytest.raises(AssertionError):
            crt(r, m)

    @pytest.mark.parametrize((
        'n', 'm', 'a', 'b'
    ), [
        (-1, 1, 0, 0),
        (0, 1, 0, 0),
        (1, 0, 0, 0),
        (1, -1, 0, 0),
    ])
    def test_floor_sum_failed_if_invalid_input_is_given(
        self, n: int, m: int, a: int, b: int
    ) -> None:
        '''
        floor_sum(n, m, a, b) is expected to be raised an AssertionError if an
        invalid input is given.

        GIVEN parameter n(< 1), m(< 1), a, b
        WHEN floor_sum(n, m, a, b) is called
        THEN raises an AssertionError
        '''

        with pytest.raises(AssertionError):
            floor_sum(n, m, a, b)
