visited = set()


def recursion(arr, i, j):
    if not 0 <= i < len(arr) or not 0 <= j < len(arr[0]):
        return 0

    if (i, j) in visited or arr[i][j] == 0:
        return 0
    visited.add((i, j))

    return 1 + \
           recursion(arr, i + 1, j) + \
           recursion(arr, i - 1, j) + \
           recursion(arr, i, j + 1) + \
           recursion(arr, i, j - 1)


def solve(arr):
    global visited
    visited = set()
    max_area = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            max_area = max(max_area, recursion(arr, i, j))

    return max_area


A = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]
print(solve(A))
