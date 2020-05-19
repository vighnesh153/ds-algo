def solve(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows == 0 or matrix[0][0] == 1:
        return 0

    result = [[0 for _ in range(cols)] for __ in range(rows)]
    result[0][0] = 1

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                continue
            if i - 1 >= 0:
                result[i][j] += result[i - 1][j]
            if j - 1 >= 0:
                result[i][j] += result[i][j - 1]

    return result[-1][-1]


A = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(solve(A))
