import typing


class SimpleQueue:
    def __init__(self):
        self._payload = []
        self._pos = 0
        self._size = 0

    def reserve(self, n: int) -> None:
        self._payload += [None] * (n - len(self._payload))

    def __len__(self) -> int:
        return self._size

    def empty(self) -> bool:
        return self._size == 0

    def push(self, t: typing.Any) -> None:
        i = self._pos + self._size
        if len(self._payload) <= i:
            self.reserve(i + 1)
        self._payload[i] = t

    def front(self) -> typing.Any:
        return self._payload[self._pos]

    def clear(self) -> None:
        self._payload = []
        self._pos = 0
        self._size = 0

    def pop(self) -> None:
        self._pos += 1
        self._size -= 1
