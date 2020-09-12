from __future__ import annotations
import copy
import typing

import atcoder._math


class ModContext:
    context = []

    def __init__(self, mod: int) -> None:
        assert 1 <= mod

        self.mod = mod

    def __enter__(self) -> None:
        self.context.append(atcoder._math.barrett(self.mod))

    def __exit__(self, exc_type: typing.Any, exc_value: typing.Any,
                 traceback: typing.Any) -> None:
        self.context.pop()

    @classmethod
    def get_bt(cls) -> int:
        return cls.context[-1]


class Modint:
    def __init__(self, v: int = 0) -> None:
        self._bt = ModContext.get_bt()
        if v == 0:
            self._v = 0
        else:
            self._v = v % self.mod()

    def mod(self) -> int:
        return self._bt.umod()

    def val(self) -> int:
        return self._v

    def __iadd__(self, rhs: Modint) -> Modint:
        self._v += rhs._v
        if self._v >= self.mod():
            self._v -= self.mod()
        return self

    def __isub__(self, rhs: Modint) -> Modint:
        self._v -= rhs._v
        if self._v < 0:
            self._v += self.mod()
        return self

    def __imul__(self, rhs: Modint) -> Modint:
        self._v = self._bt.mul(self._v, rhs._v)
        return self

    def __ifloordiv__(self, rhs: Modint) -> Modint:
        self *= rhs.inv()
        return self

    def __pos__(self) -> Modint:
        return self

    def __neg__(self) -> Modint:
        return Modint() - self

    def __pow__(self, n: int) -> Modint:
        assert 0 <= n

        x = self
        r = 1

        while n:
            if n & 1:
                r *= x
            x = x * x
            n >>= 1

        return r

    def inv(self) -> Modint:
        eg = atcoder._math._inv_gcd(self._v, self.mod())

        assert eg[0] == 1

        return eg[1]

    def __add__(self, rhs: Modint) -> Modint:
        result = copy.deepcopy(self)
        result += rhs
        return result

    def __sub__(self, rhs: Modint) -> Modint:
        result = copy.deepcopy(self)
        result -= rhs
        return result

    def __mul__(self, rhs: Modint) -> Modint:
        result = copy.deepcopy(self)
        result *= rhs
        return result

    def __floordiv__(self, rhs: Modint) -> Modint:
        result = copy.deepcopy(self)
        result //= rhs
        return result

    def __eq__(self, rhs: Modint) -> bool:
        return self._v == rhs._v

    def __ne__(self, rhs: Modint) -> bool:
        return self._v != rhs._v


def raw(v: int) -> Modint:
    x = Modint()
    x._v = v
    return x
