from math import factorial


def solve(m, n):
    return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))


print(solve(7, 3))
