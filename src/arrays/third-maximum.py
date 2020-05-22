from heapq import *


def solve(arr):
    arr = [-e for e in set(arr)]
    heapify(arr)

    if len(arr) < 3:
        return -min(arr)

    heappop(arr)
    heappop(arr)
    return -heappop(arr)


A = [2, 2, 3, 1]
print(solve(A))
