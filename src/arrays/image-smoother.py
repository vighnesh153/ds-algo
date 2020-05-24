def get_average_value(arr, i, j):
    rows = len(arr)
    cols = len(arr[0])

    s = 0
    c = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if 0 <= x + i < rows and 0 <= y + j < cols:
                s += arr[x + i][y + j]
                c += 1

    return s // c


def solve(arr):
    matrix = [[None for _ in range(len(arr[0]))] for __ in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            new_val = get_average_value(arr, i, j)
            matrix[i][j] = new_val

    return matrix


A = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
print(solve(A))
