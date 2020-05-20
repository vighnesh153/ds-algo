def solve(n):
    new_row = [1]
    prev_row = new_row

    counter = 0
    while counter != n:
        new_row = [1]
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        new_row.append(1)
        prev_row = new_row
        counter += 1

    return new_row


print(solve(10))
