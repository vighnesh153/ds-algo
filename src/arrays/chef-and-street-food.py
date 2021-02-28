# https://www.codechef.com/LRNDSA02/problems/STFOOD

for _ in range(int(input())):
    n = int(input())
    maximum = 0
    for _ in range(n):
        s, p, v = map(int, input().split())
        profit = (p // (s + 1)) * v
        maximum = max(maximum, profit)

    print(maximum)
