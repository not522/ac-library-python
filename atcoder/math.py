import typing

import atcoder._math

def pow_mod(x: int, n: int, m: int) -> int:
    return pow(x, n, m)


def inv_mod(x: int, m: int) -> int:
    assert 1 <= m

    z = atcoder._math._inv_gcd(x, m)

    assert z[0] == 1

    return z[1]


def crt(r: typing.List[int], m: typing.List[int]) -> typing.Tuple[int, int]:
    assert len(r) == len(m)

    # Contracts: 0 <= r0 < m0
    r0 = 0
    m0 = 1
    for r1, m1 in zip(r, m):
        assert 1 <= m1
        r1 %= m1
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return (0, 0)
            continue

        # assume: m0 > m1, lcm(m0, m1) >= 2 * max(m0, m1)

        '''
        (r0, m0), (r1, m1) -> (r2, m2 = lcm(m0, m1));
        r2 % m0 = r0
        r2 % m1 = r1
        -> (r0 + x*m0) % m1 = r1
        -> x*u0*g % (u1*g) = (r1 - r0) (u0*g = m0, u1*g = m1)
        -> x = (r1 - r0) / g * inv(u0) (mod u1)
        '''

        # im = inv(u0) (mod u1) (0 <= im < u1)
        g, im = atcoder._math._inv_gcd(m0, m1)

        u1 = m1 // g
        # |r1 - r0| < (m0 + m1) <= lcm(m0, m1)
        if (r1 - r0) % g:
            return (0, 0)

        # u1 * u1 <= m1 * m1 / g / g <= m0 * m1 / g = lcm(m0, m1)
        x = (r1 - r0) // g % u1 * im % u1

        '''
        |r0| + |m0 * x|
        < m0 + m0 * (u1 - 1)
        = m0 + m0 * m1 / g - m0
        = lcm(m0, m1)
        '''

        r0 += x * m0
        m0 *= u1  # -> lcm(m0, m1)
        if r0 < 0:
            r0 += m0

    return (r0, m0)


def floor_sum(n: int, m: int, a: int, b: int) -> int:
    assert 1 <= n
    assert 1 <= m

    ans = 0

    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m

    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = y_max * m - b

    if y_max == 0:
        return ans

    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)

    return ans
