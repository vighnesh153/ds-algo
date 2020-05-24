def is_sorted(_array):
    for i in range(len(_array) - 1):
        if _array[i] > _array[i + 1]:
            return False
    return True


def solve(arr):
    arr1, arr2 = arr[:], arr[:]
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr1[i] = arr[i + 1]
            arr2[i + 1] = arr[i]
            break
    return is_sorted(arr1) or is_sorted(arr2)


A = [4, 2, 1]
print(solve(A))
