# https://atcoder.jp/contests/practice2/tasks/practice2_h

import sys

from atcoder.twosat import TwoSAT


def main() -> None:
    n, d = map(int, sys.stdin.readline().split())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, sys.stdin.readline().split())

    two_sat = TwoSAT(n)

    for i in range(n):
        for j in range(i + 1, n):
            if abs(x[i] - x[j]) < d:
                two_sat.add_clause(i, False, j, False)
            if abs(x[i] - y[j]) < d:
                two_sat.add_clause(i, False, j, True)
            if abs(y[i] - x[j]) < d:
                two_sat.add_clause(i, True, j, False)
            if abs(y[i] - y[j]) < d:
                two_sat.add_clause(i, True, j, True)

    if not two_sat.satisfiable():
        print("No")
    else:
        print("Yes")
        answer = two_sat.answer()
        for i in range(n):
            if answer[i]:
                print(x[i])
            else:
                print(y[i])


if __name__ == '__main__':
    main()
