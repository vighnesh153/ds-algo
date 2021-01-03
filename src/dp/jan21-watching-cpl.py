# https://www.codechef.com/JAN21C/problems/WIPL
import sys


sys.setrecursionlimit(100001)


def integer_array_input():
    return list(map(int, input().split()))


def integer_input():
    return int(input())


def test_case_count():
    return range(integer_input())


def recursion(arr, k, solutions, i=0, s1=0, s2=0, dp=None, c=0):
    if dp is None:
        dp = set()

    if i >= len(arr):
        if s1 >= k and s2 >= k:
            solutions.add(c)
        return

    key = (s1, s2, c)

    if key in dp:
        return

    if s1 >= k and s2 >= k:
        solutions.add(c)
        return

    if s1 < k:
        recursion(arr, k, solutions, i + 1, s1 + arr[i], s2, dp, c + 1)
    if s2 < k:
        recursion(arr, k, solutions, i + 1, s1, s2 + arr[i], dp, c + 1)

    dp.add(key)


def solve(n, k, arr):
    arr.sort(reverse=True)
    solutions = set()
    recursion(arr, k, solutions)

    solutions = list(solutions)
    if len(solutions) == 0:
        print(-1)
    else:
        print(min(solutions))


def main():
    for _ in test_case_count():
        n, k = integer_array_input()
        arr = integer_array_input()
        solve(n, k, arr)


main()
