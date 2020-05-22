def solve(arr):
    i = 0
    j = 0

    while i < len(arr) and j < len(arr):
        if arr[i] != 0 and arr[j] != 0:
            i += 1
            j += 1
        elif arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[i] != 0:
            j += 1
        else:
            j += 1


A = [0, 1, 0, 3, 12]
solve(A)
print(A)
