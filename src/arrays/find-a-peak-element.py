def is_peak(arr, index):
    if index == 0:
        return arr[0] > arr[1]

    if index == len(arr) - 1:
        return arr[-1] > arr[-2]

    return arr[index] > arr[index - 1] and arr[index] > arr[index + 1]


def solve(arr):
    if len(arr) == 1:
        return 0

    low = 0
    high = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if is_peak(arr, mid):
            return mid
        else:
            if mid == 0:
                low = mid + 1
            elif mid == len(arr) - 1:
                high = mid - 1
            else:
                if arr[mid - 1] > arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1


A = [2, 1]
print(solve(A))
