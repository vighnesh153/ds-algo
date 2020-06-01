# https://www.codechef.com/problems/SALARY


def solve():
    for _ in range(int(input())):
        _ = input()
        arr = list(map(int, input().split()))

        print(sum(arr) - (len(arr) * min(arr)))


solve()
