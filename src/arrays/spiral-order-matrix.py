def solve(n):
    matrix = [[-1 for _ in range(n)] for __ in range(n)]

    curr = 1
    last = n * n
    iteration = -1
    while curr <= last:
        iteration += 1
        i = j = iteration
        while j < n - iteration:
            matrix[i][j] = curr
            curr += 1
            j += 1

        j -= 1
        i += 1
        while i < n - iteration:
            matrix[i][j] = curr
            curr += 1
            i += 1

        i -= 1
        j -= 1
        while j >= iteration:
            matrix[i][j] = curr
            curr += 1
            j -= 1

        j += 1
        i -= 1
        while i >= iteration + 1:
            matrix[i][j] = curr
            curr += 1
            i -= 1

    return matrix


res = solve(6)
for row in res:
    print(row)
