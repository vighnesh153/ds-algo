# https://www.codechef.com/JUNE20B/problems/PRICECON


def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        loss = 0
        for item in arr:
            loss += 0 if item < k else (item - k)

        print(loss)


solve()
