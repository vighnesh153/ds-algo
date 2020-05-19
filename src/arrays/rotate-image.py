def solve(matrix):
    iteration = 0
    size = len(matrix)

    while iteration < size // 2:
        # We only need to modify number of elements in that row - 1 elements
        for i in range(size - iteration * 2 - 1):
            i1 = j1 = iteration
            i2 = iteration
            j2 = size - iteration - 1
            i3 = j3 = size - iteration - 1
            i4 = size - iteration - 1
            j4 = iteration

            j1 += i
            i2 += i
            j3 -= i
            i4 -= i

            matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = \
                matrix[i4][j4], matrix[i1][j1], matrix[i2][j2], matrix[i3][j3]

        iteration += 1


A = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
solve(A)
for row in A:
    print(row)
