import typing


class Barrett:
    '''
    Fast moduler by barrett reduction
    Reference: https://en.wikipedia.org/wiki/Barrett_reduction
    NOTE: reconsider after Ice Lake
    '''

    def __init__(self, m: int) -> None:
        self._m = m
        self._im = ((1 << 64) - 1) / m + 1

    def umod(self) -> int:
        return self._m

    def mul(self, a: int, b: int) -> int:
        '''
        [1] m = 1
        a = b = im = 0, so okay

        [2] m >= 2
        im = ceil(2^64 / m)
        -> im * m = 2^64 + r (0 <= r < m)
        let z = a*b = c*m + d (0 <= c, d < m)
        a*b * im = (c*m + d) * im = c*(im*m) + d*im = c*2^64 + c*r + d*im
        c*r + d*im < m*m + m*im < m*m + 2^64 + m <= 2^64 + m*(m+1) < 2^64 * 2
        ((ab * im) >> 64) == c or c + 1
        '''

        z = a * b
        x = (z * self._im) >> 64
        v = z - x * self._m
        if self._m <= v:
            v += self._m
        return v


def _is_prime(n: int) -> bool:
    '''
    Reference:
    M. Forisek and J. Jancina,
    Fast Primality Testing for Integers That Fit into a Machine Word
    '''

    if n <= 1:
        return False
    if n == 2 or n == 7 or n == 61:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d /= 2

    for a in (2, 7, 61):
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0:
            return False
    return True


def _inv_gcd(a: int, b: int) -> typing.Tuple[int, int]:
    a %= b
    if a == 0:
        return (b, 0)

    # Contracts:
    # [1] s - m0 * a = 0 (mod b)
    # [2] t - m1 * a = 0 (mod b)
    # [3] s * |m1| + t * |m0| <= b
    s = b
    t = a
    m0 = 0
    m1 = 1

    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u  # |m1 * u| <= |m1| * s <= b

        # [3]:
        # (s - t * u) * |m1| + t * |m0 - m1 * u|
        # <= s * |m1| - t * u * |m1| + t * (|m0| + |m1| * u)
        # = s * |m1| + t * |m0| <= b

        s, t = t, s
        m0, m1 = m1, m0

    # by [3]: |m0| <= b/g
    # by g != b: |m0| < b/g
    if m0 < 0:
        m0 += b // s

    return (s, m0)


def _primitive_root(m: int) -> int:
    if m == 2:
        return 1
    if m == 167772161:
        return 3
    if m == 469762049:
        return 3
    if m == 754974721:
        return 11
    if m == 998244353:
        return 3

    divs = [2] + [0] * 19
    cnt = 1
    x = (m - 1) // 2
    while x % 2 == 0:
        x //= 2

    i = 3
    while i * i <= x:
        if x % i == 0:
            divs[cnt] = i
            cnt += 1
            while x % i == 0:
                x //= i
        i += 2

    if x > 1:
        divs[cnt] = x
        cnt += 1

    g = 2
    while True:
        for i in range(cnt):
            if pow(g, (m - 1) // divs[i], m) == 1:
                break
        else:
            return g
        g += 1
