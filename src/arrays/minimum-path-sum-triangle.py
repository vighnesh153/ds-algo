def solve(arr):
    for i in range(len(arr) - 2, -1, -1):
        for j in range(len(arr[i])):
            arr[i][j] += min(arr[i + 1][j], arr[i + 1][j + 1])

    return arr[0][0]


A = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(solve(A))
