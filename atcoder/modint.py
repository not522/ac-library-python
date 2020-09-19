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
        self.context.append(self.mod)

    def __exit__(self, exc_type: typing.Any, exc_value: typing.Any,
                 traceback: typing.Any) -> None:
        self.context.pop()

    @classmethod
    def get_mod(cls) -> int:
        return cls.context[-1]


class Modint:
    def __init__(self, v: int = 0) -> None:
        self._mod = ModContext.get_mod()
        if v == 0:
            self._v = 0
        else:
            self._v = v % self._mod

    def val(self) -> int:
        return self._v

    def __iadd__(self, rhs: typing.Union[Modint, int]) -> Modint:
        rhs = self._asmodint(rhs)
        self._v += rhs._v
        if self._v >= self._mod:
            self._v -= self._mod
        return self

    def __isub__(self, rhs: typing.Union[Modint, int]) -> Modint:
        rhs = self._asmodint(rhs)
        self._v -= rhs._v
        if self._v < 0:
            self._v += self._mod
        return self

    def __imul__(self, rhs: typing.Union[Modint, int]) -> Modint:
        rhs = self._asmodint(rhs)
        self._v = self._v * rhs._v % self._mod
        return self

    def __ifloordiv__(self, rhs: typing.Union[Modint, int]) -> Modint:
        rhs = self._asmodint(rhs)
        self *= rhs.inv()
        return self

    def __pos__(self) -> Modint:
        return self

    def __neg__(self) -> Modint:
        return Modint() - self

    def __pow__(self, n: int) -> Modint:
        assert 0 <= n

        return Modint(pow(self._v, n, self._mod))

    def inv(self) -> Modint:
        eg = atcoder._math._inv_gcd(self._v, self._mod)

        assert eg[0] == 1

        return Modint(eg[1])

    def __add__(self, rhs: typing.Union[Modint, int]) -> Modint:
        rhs = self._asmodint(rhs)
        result = copy.deepcopy(self)
        result += rhs
        return result

    def __sub__(self, rhs: typing.Union[Modint, int]) -> Modint:
        rhs = self._asmodint(rhs)
        result = copy.deepcopy(self)
        result -= rhs
        return result

    def __mul__(self, rhs: typing.Union[Modint, int]) -> Modint:
        rhs = self._asmodint(rhs)
        result = copy.deepcopy(self)
        result *= rhs
        return result

    def __floordiv__(self, rhs: typing.Union[Modint, int]) -> Modint:
        rhs = self._asmodint(rhs)
        result = copy.deepcopy(self)
        result //= rhs
        return result

    def __eq__(self, rhs: typing.Union[Modint, int]) -> bool:
        rhs = self._asmodint(rhs)
        return self._v == rhs._v

    def __ne__(self, rhs: typing.Union[Modint, int]) -> bool:
        rhs = self._asmodint(rhs)
        return self._v != rhs._v

    def _asmodint(self, rhs: typing.Union[Modint, int]) -> Modint:
        if isinstance(rhs, Modint):
            return rhs
        else:
            return Modint(rhs)


def raw(v: int) -> Modint:
    x = Modint()
    x._v = v
    return x
