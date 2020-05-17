def solve(matrix, element):
    arr = []
    for row in matrix:
        arr += row

    arr.sort()

    median_index = len(arr) // 2
    median1 = arr[median_index]
    median2 = arr[median_index - 1] \
        if 0 <= median_index - 1 < len(arr) \
        else -1

    count1 = 0
    count2 = 0 if median2 != -1 else float('inf')
    for elem in arr:
        if (elem - median1) % element != 0:
            return -1
        count1 += abs(elem - median1) // element

        if median2 != -1:
            if (elem - median2) % element != 0:
                return -1
            count2 += abs(elem - median2) // element

    return min(count1, count2)


A = [
    [0, 2, 8],
    [8, 2, 0],
    [0, 2, 8]
]
B = 2
print(solve(A, B))
