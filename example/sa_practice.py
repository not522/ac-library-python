# https://atcoder.jp/contests/practice2/tasks/practice2_i

import sys

from atcoder.string import suffix_array, lcp_array


def main() -> None:
    s = sys.stdin.readline().strip()
    sa = suffix_array(s)

    answer = len(s) * (len(s) + 1) // 2
    for x in lcp_array(s, sa):
        answer -= x
    print(answer)


if __name__ == '__main__':
    main()
