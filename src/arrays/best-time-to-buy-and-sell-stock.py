def solve(arr):
    suffix_max = [0] * len(arr)
    for i in range(len(arr) - 2, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1], arr[i + 1])

    max_profit = -float('inf')
    for i in range(len(arr)):
        max_profit = max(max_profit, suffix_max[i] - arr[i])

    return max(0, max_profit)


A = [7, 6, 4, 3, 1]
print(solve(A))
