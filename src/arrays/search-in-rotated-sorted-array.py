def solve(arr: [int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            if target <= arr[-1] < arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if target >= arr[0] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


A = [4, 5, 6, 7, 0, 1, 2]
B = 3
print(solve(A, B))
