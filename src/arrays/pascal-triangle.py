def solve(n):
    result = []

    while len(result) != n:
        if len(result) == 0:
            result.append([1])
        else:
            row = [1]
            prev_row = result[-1]
            for i in range(0, len(prev_row) - 1):
                row.append(prev_row[i] + prev_row[i + 1])
            row.append(1)
            result.append(row)

    return result


for _row in solve(10):
    print(_row)
