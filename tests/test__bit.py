import pytest

from atcoder._bit import _ceil_pow2, _bsf


class TestInternalBit:

    @pytest.mark.parametrize((
        'n', 'expected'
        ), [
        (0, 0),
        (1, 0),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 3),
        (6, 3),
        (7, 3),
        (8, 3),
        (9, 4),
        ((1 << 30) - 1, 30),
        (1 << 30, 30),
        ((1 << 30) + 1, 31),
        ((1 << 100) - 1, 100),
        (1 << 100, 100),
        ((1 << 100) + 1, 101),
    ])
    def test_ceil_pow2(self, n: int, expected: int) -> None:
        assert _ceil_pow2(n) == expected

    @pytest.mark.parametrize((
        'n', 'expected'
        ), [
        (1, 0),
        (2, 1),
        (3, 0),
        (4, 2),
        (5, 0),
        (6, 1),
        (7, 0),
        (8, 3),
        (9, 0),
        ((1 << 30) - 1, 0),
        (1 << 30, 30),
        ((1 << 30) + 1, 0),
        ((1 << 31) - 1, 0),
        (1 << 31, 31),
        ((1 << 31) + 1, 0),
        ((1 << 100) - 1, 0),
        (1 << 100, 100),
        ((1 << 100) + 1, 0),
    ])
    def test_bsf(self, n: int, expected: int) -> None:
        assert _bsf(n) == expected
