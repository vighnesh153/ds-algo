def solve(arr):
    prefix_max = [0] * len(arr)
    for i in range(1, len(arr)):
        prefix_max[i] = max(prefix_max[i - 1], arr[i - 1])

    suffix_max = [0] * len(arr)
    for j in range(len(arr) - 2, -1, -1):
        suffix_max[j] = max(suffix_max[j + 1], arr[j + 1])

    area = 0
    for i, elem in enumerate(arr):
        current_area = min(prefix_max[i], suffix_max[i]) - elem
        if current_area > 0:
            area += current_area

    return area


res = solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(res)
