import typing

import atcoder._bit
import atcoder._math
from atcoder.modint import ModContext, Modint


_sum_e = {}  # _sum_e[i] = ies[0] * ... * ies[i - 1] * es[i]


def _butterfly(a: typing.List[Modint]) -> None:
    g = atcoder._math._primitive_root(a[0].mod())
    n = len(a)
    h = atcoder._bit._ceil_pow2(n)

    if a[0].mod() not in _sum_e:
        es = [Modint(0)] * 30  # es[i]^(2^(2+i)) == 1
        ies = [Modint(0)] * 30
        cnt2 = atcoder._bit._bsf(a[0].mod() - 1)
        e = Modint(g) ** ((a[0].mod() - 1) >> cnt2)
        ie = e.inv()
        for i in range(cnt2, 1, -1):
            # e^(2^i) == 1
            es[i - 2] = e
            ies[i - 2] = ie
            e = e * e
            ie = ie * ie
        sum_e = [Modint(0)] * 30
        now = Modint(1)
        for i in range(cnt2 - 2):
            sum_e[i] = es[i] * now
            now *= ies[i]
        _sum_e[a[0].mod()] = sum_e
    else:
        sum_e = _sum_e[a[0].mod()]

    for ph in range(1, h + 1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        now = Modint(1)
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                left = a[i + offset]
                right = a[i + offset + p] * now
                a[i + offset] = left + right
                a[i + offset + p] = left - right
            now *= sum_e[atcoder._bit._bsf(~s)]


_sum_ie = {}  # _sum_ie[i] = es[0] * ... * es[i - 1] * ies[i]


def _butterfly_inv(a: typing.List[Modint]) -> None:
    g = atcoder._math._primitive_root(a[0].mod())
    n = len(a)
    h = atcoder._bit._ceil_pow2(n)

    if a[0].mod() not in _sum_ie:
        es = [Modint(0)] * 30  # es[i]^(2^(2+i)) == 1
        ies = [Modint(0)] * 30
        cnt2 = atcoder._bit._bsf(a[0].mod() - 1)
        e = Modint(g) ** ((a[0].mod() - 1) >> cnt2)
        ie = e.inv()
        for i in range(cnt2, 1, -1):
            # e^(2^i) == 1
            es[i - 2] = e
            ies[i - 2] = ie
            e = e * e
            ie = ie * ie
        sum_ie = [Modint(0)] * 30
        now = Modint(1)
        for i in range(cnt2 - 2):
            sum_ie[i] = ies[i] * now
            now *= es[i]
        _sum_ie[a[0].mod()] = sum_ie
    else:
        sum_ie = _sum_ie[a[0].mod()]

    for ph in range(h, 0, -1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        inow = Modint(1)
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                left = a[i + offset]
                right = a[i + offset + p]
                a[i + offset] = left + right
                a[i + offset + p] = Modint(
                    (a[0].mod() + left.val() - right.val()) * inow.val())
            inow *= sum_ie[atcoder._bit._bsf(~s)]


def convolution_mod(a: typing.List[Modint],
                    b: typing.List[Modint]) -> typing.List[Modint]:
    n = len(a)
    m = len(b)

    if n == 0 or m == 0:
        return []

    if min(n, m) <= 60:
        if n < m:
            n, m = m, n
            a, b = b, a
        ans = [Modint(0) for _ in range(n + m - 1)]
        for i in range(n):
            for j in range(m):
                ans[i + j] += a[i] * b[j]
        return ans

    z = 1 << atcoder._bit._ceil_pow2(n + m - 1)

    while len(a) < z:
        a.append(Modint(0))
    _butterfly(a)

    while len(b) < z:
        b.append(Modint(0))
    _butterfly(b)

    for i in range(z):
        a[i] *= b[i]
    _butterfly_inv(a)
    a = a[:n + m - 1]

    iz = Modint(z).inv()
    for i in range(n + m - 1):
        a[i] *= iz

    return a


def convolution(mod: int, a: typing.List[typing.Any],
                b: typing.List[typing.Any]) -> typing.List[typing.Any]:
    n = len(a)
    m = len(b)

    if n == 0 or m == 0:
        return []

    with ModContext(mod):
        a2 = list(map(Modint, a))
        b2 = list(map(Modint, b))

        return list(map(lambda c: c.val(), convolution_mod(a2, b2)))


def convolution_int(
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
        c[i] += (c1[i] * i1) % mod1 * m2m3
        c[i] += (c2[i] * i2) % mod2 * m1m3
        c[i] += (c3[i] * i3) % mod3 * m1m2
        c[i] %= m1m2m3

    return c
