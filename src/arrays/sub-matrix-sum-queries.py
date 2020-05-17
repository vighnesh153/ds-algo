modulo = 10 ** 9 + 7


def solve(matrix, top_x, top_y, bottom_x, bottom_y):
    for row in matrix:
        for i in range(1, len(row)):
            row[i] += row[i - 1]

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] += matrix[i - 1][j]

    result = []
    for i in range(len(top_x)):
        top_left_x, top_left_y = top_x[i] - 1, top_y[i] - 1
        bottom_right_x, bottom_right_y = bottom_x[i] - 1, bottom_y[i] - 1

        s = matrix[bottom_right_x][bottom_right_y]

        if top_left_x - 1 >= 0:
            s -= matrix[top_left_x - 1][bottom_right_y]

        if top_left_y - 1 >= 0:
            s -= matrix[bottom_right_x][top_left_y - 1]

        if top_left_y - 1 >= 0 and top_left_x - 1 >= 0:
            s += matrix[top_left_x - 1][top_left_y - 1]

        result.append((s + modulo) % modulo)

    return result


res = solve(
    [[5, 17, 100, 11],
     [0, 0, 2, 8]],
    [1, 1],
    [1, 4],
    [2, 2],
    [2, 4]
)
print(res)
