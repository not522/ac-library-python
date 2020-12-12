import pytest

from atcoder._math import _is_prime, _inv_gcd, _primitive_root


class TestInternalMath:

    def test_is_prime(self) -> None:
        assert not _is_prime(-2)
        assert not _is_prime(-1)
        assert not _is_prime(121)
        assert not _is_prime(11 * 13)
        assert not _is_prime(701928443)
        assert _is_prime(998244353)
        assert not _is_prime(1_000_000_000)
        assert _is_prime(1_000_000_007)
        assert not _is_prime(1_000_000_008)
        assert _is_prime(1_000_000_009)

        for i in range(10000 + 1):
            assert _is_prime(i) == self._is_prime_naive(i)

    def _is_prime_naive(self, n: int) -> bool:
        from math import sqrt

        assert 0 <= n

        if (n == 0) or (n == 1):
            return False

        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                return False

        return True

    @pytest.mark.parametrize((
        'a', 'b', 'expected'
        ), [
        (0, 1, 1),
        (0, 4, 4),
        (0, 7, 7),
        (2, 3, 1),
        (-2, 3, 1),
        (4, 6, 2),
        (-4, 6, 2),
        (13, 23, 1),
        (57, 81, 3),
        (12345, 67890, 15),
        (-3141592 * 6535, 3141592 * 8979, 3141592),
    ])
    def test_inv_gcd(self, a: int, b: int, expected: int) -> None:
        s, m0 = _inv_gcd(a, b)
        assert s == expected
        assert (((m0 * a) % b + b) % b) == (s % b)

    def test_primitive_root(self) -> None:
        for m in range(2, 5000 + 1):
            if not _is_prime(m):
                continue

            n = _primitive_root(m)
            assert 1 <= n
            assert n < m

            x = 1

            for i in range(1, (m - 2) + 1):
                x = x * n % m
                # x == n ^ i
                assert x != 1

            x = x * n % m
            assert x == 1
