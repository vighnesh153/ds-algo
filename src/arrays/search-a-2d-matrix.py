def solve(arr, target):
    if len(arr) == 0 or len(arr[0]) == 0:
        return False

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid][0] == target:
            return True
        elif target < arr[mid][0]:
            high = mid - 1
        else:
            if target > arr[mid][-1]:
                low = mid + 1
            else:
                low = mid
                break

    if low > high:
        return False

    row = arr[low]

    low = 0
    high = len(row) - 1
    while low <= high:
        mid = (low + high) // 2

        if row[mid] == target:
            return True
        elif target < row[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


A = [
    [1]
]
B = 2
print(solve(A, B))
