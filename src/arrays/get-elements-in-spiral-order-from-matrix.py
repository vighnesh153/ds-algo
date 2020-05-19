def solve(matrix):
    if len(matrix) == 0:
        return

    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    iteration = 0
    while iteration < (cols + 1) // 2:
        i = j = iteration
        if j >= cols - iteration:
            break
        while j < cols - iteration:
            result.append(matrix[i][j])
            j += 1

        i += 1
        j -= 1
        if i >= rows - iteration:
            break
        while i < rows - iteration:
            result.append(matrix[i][j])
            i += 1

        j -= 1
        i -= 1
        if j < iteration:
            break
        while j >= iteration:
            result.append(matrix[i][j])
            j -= 1

        i -= 1
        j += 1
        if i < iteration + 1:
            break
        while i >= iteration + 1:
            result.append(matrix[i][j])
            i -= 1

        iteration += 1

    return result


A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(solve(A))
