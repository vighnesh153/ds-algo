def solve(n):
    result = [[0 for _ in range(n)] for __ in range(n)]

    counter = 1
    iteration = 0
    while counter <= n * n:
        i = j = iteration
        while j < n - iteration:
            result[i][j] = counter
            counter += 1
            j += 1

        j -= 1
        i += 1
        while i < n - iteration:
            result[i][j] = counter
            counter += 1
            i += 1

        i -= 1
        j -= 1
        while j >= iteration:
            result[i][j] = counter
            counter += 1
            j -= 1

        j += 1
        i -= 1
        while i > iteration:
            result[i][j] = counter
            counter += 1
            i -= 1

        iteration += 1

    return result


for row in solve(10):
    print(row)
