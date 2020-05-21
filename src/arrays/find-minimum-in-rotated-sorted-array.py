def solve(arr):
    low = 0
    high = len(arr) - 1

    index = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < arr[index]:
            index = mid
            if arr[mid] > arr[-1]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[mid] < arr[0]:
                high = mid - 1
            else:
                low = mid + 1

    return arr[index]


A = [4, 5, 6, 7, 0, 1, 2]
print(solve(A))
