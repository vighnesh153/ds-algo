# https://www.codechef.com/LRNDSA01/problems/CONFLIP

for _ in range(int(input())):
    for _ in range(int(input())):
        i, n, q = map(int, input().split())
        print(n // 2 + (0 if n % 2 == 0 else abs(i - q)))
