import functools
import typing


def _sa_naive(s: typing.List[int]) -> typing.List[int]:
    sa = list(range(len(s)))
    return sorted(sa, key=lambda i: s[i:])


def _sa_doubling(s: typing.List[int]) -> typing.List[int]:
    n = len(s)
    sa = list(range(n))
    rnk = s.copy()
    tmp = [0] * n
    k = 1
    while k < n:
        def cmp(x: int, y: int) -> int:
            if rnk[x] != rnk[y]:
                return rnk[x] - rnk[y]
            rx = rnk[x + k] if x + k < n else -1
            ry = rnk[y + k] if y + k < n else -1
            return rx - ry
        sa.sort(key=functools.cmp_to_key(cmp))
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (1 if cmp(sa[i - 1], sa[i]) else 0)
        tmp, rnk = rnk, tmp
        k *= 2
    return sa


def _sa_is(s: typing.List[int], upper: int) -> typing.List[int]:
    threshold_naive = 10
    threshold_doubling = 40

    n = len(s)

    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        if s[0] < s[1]:
            return [0, 1]
        else:
            return [1, 0]

    if n < threshold_naive:
        return _sa_naive(s)
    if n < threshold_doubling:
        return _sa_doubling(s)

    sa = [0] * n
    ls = [False] * n
    for i in range(n - 2, -1, -1):
        if s[i] == s[i + 1]:
            ls[i] = ls[i + 1]
        else:
            ls[i] = s[i] < s[i + 1]

    sum_l = [0] * (upper + 1)
    sum_s = [0] * (upper + 1)
    for i in range(n):
        if not ls[i]:
            sum_s[s[i]] += 1
        else:
            sum_l[s[i] + 1] += 1
    for i in range(upper + 1):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i + 1] += sum_s[i]

    def induce(lms: typing.List[int]) -> None:
        nonlocal sa
        sa = [-1] * n

        buf = sum_s.copy()
        for d in lms:
            if d == n:
                continue
            sa[buf[s[d]]] = d
            buf[s[d]] += 1

        buf = sum_l.copy()
        sa[buf[s[n - 1]]] = n - 1
        buf[s[n - 1]] += 1
        for i in range(n):
            v = sa[i]
            if v >= 1 and not ls[v - 1]:
                sa[buf[s[v - 1]]] = v - 1
                buf[s[v - 1]] += 1

        buf = sum_l.copy()
        for i in range(n - 1, -1, -1):
            v = sa[i]
            if v >= 1 and ls[v - 1]:
                buf[s[v - 1] + 1] -= 1
                sa[buf[s[v - 1] + 1]] = v - 1

    lms_map = [-1] * (n + 1)
    m = 0
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms_map[i] = m
            m += 1
    lms = []
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms.append(i)

    induce(lms)

    if m:
        sorted_lms = []
        for v in sa:
            if lms_map[v] != -1:
                sorted_lms.append(v)
        rec_s = [0] * m
        rec_upper = 0
        rec_s[lms_map[sorted_lms[0]]] = 0
        for i in range(1, m):
            left = sorted_lms[i - 1]
            right = sorted_lms[i]
            if lms_map[left] + 1 < m:
                end_l = lms[lms_map[left] + 1]
            else:
                end_l = n
            if lms_map[right] + 1 < m:
                end_r = lms[lms_map[right] + 1]
            else:
                end_r = n

            same = True
            if end_l - left != end_r - right:
                same = False
            else:
                while left < end_l:
                    if s[left] != s[right]:
                        break
                    left += 1
                    right += 1
                if left == n or s[left] != s[right]:
                    same = False

            if not same:
                rec_upper += 1
            rec_s[lms_map[sorted_lms[i]]] = rec_upper

        rec_sa = _sa_is(rec_s, rec_upper)

        for i in range(m):
            sorted_lms[i] = lms[rec_sa[i]]
        induce(sorted_lms)

    return sa


def suffix_array(s: typing.Union[str, typing.List[int]],
                 upper: typing.Optional[int] = None) -> typing.List[int]:
    '''
    SA-IS, linear-time suffix array construction
    Reference:
    G. Nong, S. Zhang, and W. H. Chan,
    Two Efficient Algorithms for Linear Time Suffix Array Construction
    '''

    if isinstance(s, str):
        return _sa_is([ord(c) for c in s], 255)
    elif upper is None:
        n = len(s)
        idx = list(range(n))

        def cmp(left: int, right: int) -> int:
            return typing.cast(int, s[left]) - typing.cast(int, s[right])

        idx.sort(key=functools.cmp_to_key(cmp))
        s2 = [0] * n
        now = 0
        for i in range(n):
            if i and s[idx[i - 1]] != s[idx[i]]:
                now += 1
            s2[idx[i]] = now
        return _sa_is(s2, now)
    else:
        assert 0 <= upper
        for d in s:
            assert 0 <= d <= upper

        return _sa_is(s, upper)


def lcp_array(s: typing.Union[str, typing.List[int]],
              sa: typing.List[int]) -> typing.List[int]:
    '''
    Longest-Common-Prefix computation
    Reference:
    T. Kasai, G. Lee, H. Arimura, S. Arikawa, and K. Park,
    Linear-Time Longest-Common-Prefix Computation in Suffix Arrays and Its
    Applications
    '''

    if isinstance(s, str):
        s = [ord(c) for c in s]

    n = len(s)
    assert n >= 1

    rnk = [0] * n
    for i in range(n):
        rnk[sa[i]] = i

    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rnk[i] == 0:
            continue
        j = sa[rnk[i] - 1]
        while j + h < n and i + h < n:
            if s[j + h] != s[i + h]:
                break
            h += 1
        lcp[rnk[i] - 1] = h

    return lcp


def z_algorithm(s: typing.Union[str, typing.List[int]]) -> typing.List[int]:
    '''
    Z algorithm
    Reference:
    D. Gusfield,
    Algorithms on Strings, Trees, and Sequences: Computer Science and
    Computational Biology
    '''

    if isinstance(s, str):
        s = [ord(c) for c in s]

    n = len(s)
    if n == 0:
        return []

    z = [0] * n
    j = 0
    for i in range(1, n):
        z[i] = 0 if j + z[j] <= i else min(j + z[j] - i, z[i - j])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if j + z[j] < i + z[i]:
            j = i
    z[0] = n

    return z
