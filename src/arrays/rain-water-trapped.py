def solve(arr):
    left_max = [0] * len(arr)
    right_max = [0] * len(arr)

    curr_max = -1
    for i in range(1, len(arr)):
        curr_max = max(curr_max, arr[i - 1])
        left_max[i] = curr_max

    curr_max = -1
    for i in range(len(arr) - 2, -1, -1):
        curr_max = max(curr_max, arr[i + 1])
        right_max[i] = curr_max

    total = 0
    for i in range(1, len(arr) - 1):
        height = min(left_max[i], right_max[i])
        water_trapped = height - arr[i]
        if water_trapped >= 0:
            total += water_trapped

    return total


res = solve([1, 2])
print(res)
