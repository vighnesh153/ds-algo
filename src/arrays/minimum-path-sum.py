def solve(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == 0 and j == 0:
                continue
            if i == 0:
                arr[i][j] += arr[i][j - 1]
                continue
            if j == 0:
                arr[i][j] += arr[i - 1][j]
                continue
            arr[i][j] += min(arr[i - 1][j], arr[i][j - 1])

    return arr[-1][-1]


A = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(solve(A))
