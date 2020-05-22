def solve(threshold, arr):
    if len(arr) == 0:
        return 0

    length = float('inf')

    i = j = 0
    prev_i = prev_j = None
    s = arr[0]
    while True:
        if (i, j) == (prev_i, prev_j):
            break
        prev_i, prev_j = i, j
        if s >= threshold:
            length = min(length, j - i + 1)
            if i + 1 < len(arr):
                s -= arr[i]
                i += 1
        else:
            if j + 1 < len(arr):
                j += 1
                s += arr[j]

        if i == len(arr) - 1 and j == len(arr) - 1:
            break

    return 0 if length == float('inf') else length


A = [1, 2, 3, 4, 5]
print(solve(11, A))
