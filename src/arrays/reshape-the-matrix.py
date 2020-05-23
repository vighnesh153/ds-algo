def solve(arr, r, c):
    original_rows = len(arr)
    original_cols = len(arr[0])

    if original_cols * original_rows != r * c:
        return arr

    new_matrix = [[None for _ in range(c)] for _ in range(r)]

    o_i = o_j = 0
    i = j = 0
    while i < r:
        new_matrix[i][j] = arr[o_i][o_j]
        j += 1
        o_j += 1
        if j == c:
            i += 1
            j = 0
        if o_j == original_cols:
            o_i += 1
            o_j = 0

    return new_matrix


A = [
    [1, 2],
    [3, 4]
]
print(solve(A, 2, 4))
