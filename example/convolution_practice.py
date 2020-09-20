# https://atcoder.jp/contests/practice2/tasks/practice2_f

import sys

from atcoder.convolution import convolution


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    c = convolution(998244353, a, b)

    print(' '.join(map(str, c)))


if __name__ == '__main__':
    main()
