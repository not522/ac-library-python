# https://atcoder.jp/contests/practice2/tasks/practice2_f

import sys

from atcoder.convolution import convolution_int


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    c = convolution_int(a, b)

    print(' '.join([str(ci % 998244353) for ci in c]))


if __name__ == '__main__':
    main()
