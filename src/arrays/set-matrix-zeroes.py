def solve(matrix):
    r_count = len(matrix)
    c_count = len(matrix[0])

    is_first_row_zero = False
    for elem in matrix[0]:
        if elem == 0:
            is_first_row_zero = True

    is_first_col_zero = False
    for i in range(r_count):
        if matrix[i][0] == 0:
            is_first_col_zero = True

    for i in range(r_count):
        for j in range(c_count):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    if not is_first_col_zero and not is_first_row_zero:
        matrix[0][0] = 1

    for i in range(1, r_count):
        if matrix[i][0] == 0:
            matrix[i] = [0] * c_count

    for j in range(1, c_count):
        if matrix[0][j] == 0:
            for i in range(1, r_count):
                matrix[i][j] = 0

    if is_first_row_zero:
        matrix[0] = [0] * c_count

    if is_first_col_zero:
        for i in range(1, r_count):
            matrix[i][0] = 0

    return matrix


res = solve([
    [1, 0],
    [1, 1]
])

for row in res:
    print(row)
