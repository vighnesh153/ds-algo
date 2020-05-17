def solve(matrix):
    s = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            top_left_choices = (i + 1) * (j + 1)
            bottom_right_choices = (rows - i) * (cols - j)
            s += bottom_right_choices * top_left_choices * matrix[i][j]
    return s


res = solve([
    [1, 1],
    [1, 1]
])
print(res)
