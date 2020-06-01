YES = "LuckyChef"
NO = "UnluckyChef"


def solve():
    for _ in range(int(input())):
        x, y, k, n = map(int, input().split())
        arr = []
        for __ in range(n):
            arr.append(list(map(int, input().split())))

        remaining_pages = x - y
        if remaining_pages <= 0:
            print(YES)
            continue

        for pages, price in arr:
            if pages >= remaining_pages and price <= k:
                print(YES)
                break
        else:
            print(NO)


solve()
