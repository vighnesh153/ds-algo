# https://www.codechef.com/SEPT20B/problems/TREE2


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    c = 0
    while len(arr) > 0 and arr[-1] > 0:
        last = arr[-1]
        while arr and arr[-1] == last:
            arr.pop()
        c += 1
    print(c)
