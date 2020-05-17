def solve(matrix, target):
    possible_results = []

    for r, row in enumerate(matrix):
        start = 0
        end = len(row) - 1

        while start <= end:
            mid = (start + end) // 2

            if row[mid] == target:
                possible_results.append((r + 1) * 1009 + mid + 1)
                break
            elif row[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

    if len(possible_results) == 0:
        return -1
    return min(possible_results)
