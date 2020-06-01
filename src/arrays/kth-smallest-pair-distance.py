from typing import List


def get_count(arr, mid):
    i = j = count = 0
    while i < len(arr):
        while j < len(arr) and arr[j] - arr[i] <= mid:
            j += 1
        count += j - i - 1
        i += 1
    return count


def solve(arr: List, k: int):
    arr.sort()

    low = 0
    high = arr[-1] - arr[0]
    possible = float('inf')

    while low <= high:
        mid = (low + high) // 2

        if get_count(arr, mid) >= k:
            possible = min(possible, mid)
            high = mid - 1
        else:
            low = mid + 1

    return possible


A = [1, 6, 1]
B = 3
print(solve(A, B))
