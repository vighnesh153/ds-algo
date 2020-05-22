def solve(arr):
    for i in range(len(arr)):
        index = abs(arr[i]) - 1
        arr[index] = -abs(arr[index])

    return [i + 1 for i in range(len(arr)) if arr[i] > 0]


A = [4, 3, 2, 7, 8, 2, 3, 1]
print(solve(A))
