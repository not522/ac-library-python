import typing

import atcoder._bit
import atcoder._math
import atcoder.modint
from atcoder.modint import modint


_sum_e = {}  # _sum_e[i] = ies[0] * ... * ies[i - 1] * es[i]


def _butterfly(a: typing.List[modint]) -> None:
    g = atcoder._math._primitive_root(a[0].mod())
    n = len(a)
    h = atcoder._bit._ceil_pow2(n)

    if a[0].mod() not in _sum_e:
        es = [0] * 30  # es[i]^(2^(2+i)) == 1
        ies = [0] * 30
        cnt2 = atcoder._bit._bsf(a[0].mod() - 1)
        e = modint(g).pow((a[0].mod() - 1) >> cnt2)
        ie = e.inv()
        for i in range(cnt2, 1, -1):
            # e^(2^i) == 1
            es[i - 2] = e
            ies[i - 2] = ie
            e *= e
            ie *= ie
        sum_e = [0] * 30
        now = modint(1)
        for i in range(cnt2 - 2):
            sum_e[i] = es[i] * now
            now *= ies[i]
        _sum_e[a[0].mod()] = sum_e
    else:
        sum_e = _sum_e[a[0].mod()]

    for ph in (1, h + 1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        now = modint(1)
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                left = a[i + offset]
                right = a[i + offset + p] * now
                a[i + offset] = left + right
                a[i + offset + p] = left - right
            now *= sum_e[atcoder._bit._bsf(~s)]


_sum_ie = {}  # _sum_ie[i] = es[0] * ... * es[i - 1] * ies[i]


def _butterfly_inv(a: typing.List[modint]) -> None:
    g = atcoder._math._primitive_root(a[0].mod())
    n = len(a)
    h = atcoder._bit.ceil_pow2(n)

    if a[0].mod() not in _sum_ie:
        es = [0] * 30  # es[i]^(2^(2+i)) == 1
        ies = [0] * 30
        cnt2 = atcoder._bit._bsf(a[0].mod() - 1)
        e = modint(g).pow((a[0].mod() - 1) >> cnt2)
        ie = e.inv()
        for i in range(cnt2, 1, -1):
            # e^(2^i) == 1
            es[i - 2] = e
            ies[i - 2] = ie
            e *= e
            ie *= ie
        sum_ie = [0] * 30
        now = modint(1)
        for i in range(cnt2 - 2):
            sum_ie[i] = ies[i] * now
            now *= es[i]
        _sum_ie[a[0].mod()] = sum_ie
    else:
        sum_ie = _sum_ie[a[0].mod()]

    for ph in range(h, 0, -1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        inow = modint(1)
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                left = a[i + offset]
                right = a[i + offset + p]
                a[i + offset] = left + right
                a[i + offset + p] = (a[0].mod() +
                                     left.val() - right.val()) * inow.val()
            inow *= sum_ie[atcoder._bit._bsf(~s)]


def convolution_mod(a: typing.List[modint],
                    b: typing.List[modint]) -> typing.List[modint]:
    n = len(a)
    m = len(b)

    if n == 0 or m == 0:
        return []

    if min(n, m) <= 60:
        if n < m:
            n, m = m, n
            a, b = b, a
        ans = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                ans[i + j] += a[i] * b[j]
        return ans

    z = 1 << atcoder._bit._ceil_pow2(n + m - 1)

    while len(a) < z:
        a.append(modint(0))
    _butterfly(a)

    while len(b) < z:
        b.append(modint(0))
    _butterfly(b)

    for i in range(z):
        a[i] *= b[i]
    _butterfly_inv(a)
    a = a[:n + m - 1]

    iz = modint(z).inv()
    for i in range(n + m - 1):
        a[i] *= iz

    return a


def convolution(mod: int, a: typing.List[typing.Any],
                b: typing.List[typing.Any]) -> typing.List[typing.Any]:
    n = len(a)
    m = len(b)

    if n == 0 or m == 0:
        return []

    atcoder.modint.set_mod(mod)

    a2 = map(modint, a)
    b2 = map(modint, b)

    return list(map(lambda c: c.val(), convolution_mod(a2, b2)))


def convolution_ll(
        a: typing.List[int], b: typing.List[int]) -> typing.List[int]:
    n = len(a)
    m = len(b)

    if n == 0 or m == 0:
        return []

    mod1 = 754974721  # 2^24
    mod2 = 167772161  # 2^25
    mod3 = 469762049  # 2^26
    m2m3 = mod2 * mod3
    m1m3 = mod1 * mod3
    m1m2 = mod1 * mod2
    m1m2m3 = mod1 * mod2 * mod3

    i1 = atcoder._math._inv_gcd(mod2 * mod3, mod1)[1]
    i2 = atcoder._math._inv_gcd(mod1 * mod3, mod2)[1]
    i3 = atcoder._math._inv_gcd(mod1 * mod2, mod3)[1]

    c1 = convolution(mod1, a, b)
    c2 = convolution(mod2, a, b)
    c3 = convolution(mod3, a, b)

    c = [0] * (n + m - 1)
    for i in range(n + m - 1):
        x = 0
        x += (c1[i] * i1) % mod1 * m2m3
        x += (c2[i] * i2) % mod2 * m1m3
        x += (c3[i] * i3) % mod3 * m1m2

        '''
        B = 2^63, -B <= x, r(real value) < B
        (x, x - M, x - 2M, or x - 3M) = r (mod 2B)
        r = c1[i] (mod MOD1)
        focus on MOD1
        r = x, x - M', x - 2M', x - 3M' (M' = M % 2^64) (mod 2B)
        r = x,
            x - M' + (0 or 2B),
            x - 2M' + (0, 2B or 4B),
            x - 3M' + (0, 2B, 4B or 6B) (without mod!)
        (r - x) = 0, (0)
                  - M' + (0 or 2B), (1)
                  -2M' + (0 or 2B or 4B), (2)
                  -3M' + (0 or 2B or 4B or 6B) (3) (mod MOD1)
        we checked that
          ((1) mod MOD1) mod 5 = 2
          ((2) mod MOD1) mod 5 = 3
          ((3) mod MOD1) mod 5 = 4
        '''

        diff = c1[i] - x % mod1
        if diff < 0:
            diff += mod1
        offset = [0, 0, m1m2m3, 2 * m1m2m3, 3 * m1m2m3]
        x -= offset[diff % 5]
        c[i] = x

    return c
