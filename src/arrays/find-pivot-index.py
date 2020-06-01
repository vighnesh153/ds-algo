def solve(arr):
    prefix = [0] * len(arr)
    for i in range(1, len(arr)):
        prefix[i] = arr[i - 1] + prefix[i - 1]

    suffix = [0] * len(arr)
    for i in range(len(arr) - 2, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i + 1]

    for i in range(len(arr)):
        if suffix[i] == prefix[i]:
            return i

    return -1


A = [1, 7, 3, 6, 5, 6]
print(solve(A))
