def find_left(arr: [int], target: int):
    position = float('inf')

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if target <= arr[mid]:
            if arr[mid] == target:
                position = min(position, mid)
            high = mid - 1
        else:
            low = mid + 1

    return -1 if position == float('inf') else position


def find_right(arr: [int], target: int):
    position = -float('inf')

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if target >= arr[mid]:
            if arr[mid] == target:
                position = max(position, mid)
            low = mid + 1
        else:
            high = mid - 1

    return -1 if position == -float('inf') else position


def solve(arr, target):
    return [find_left(arr, target), find_right(arr, target)]


A = [5, 7, 7, 8, 8, 10]
B = 8
print(solve(A, B))
