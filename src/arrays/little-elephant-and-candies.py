def solve():
    for _ in range(int(input())):
        e, c = map(int, input().split())
        arr = list(map(int, input().split()))

        if sum(arr) <= c:
            print('Yes')
        else:
            print('No')


solve()
