def get_max_from_suffix_and_array(suffix, arr):
    max_profit = 0
    for i in range(len(arr)):
        max_profit = max(max_profit, suffix[i] - arr[i])
    return max_profit


def single_selling(arr):
    suffix_max = [0] * len(arr)
    for i in range(len(arr) - 2, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1], arr[i + 1])

    return get_max_from_suffix_and_array(suffix_max, arr)


def double_selling(arr):
    suffix_max = [0] * len(arr)
    for i in range(len(arr) - 2, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1], arr[i + 1])

    second_selling = [0] * len(arr)
    for i in range(len(arr) - 2, -1, -1):
        second_selling[i] = max(second_selling[i + 1], suffix_max[i] - arr[i])

    for i in range(len(arr)):
        second_selling[i] += arr[i]

    second_selling_suffix_max = [0] * len(arr)
    for i in range(len(arr) - 2, -1, -1):
        second_selling_suffix_max[i] = max(
            second_selling_suffix_max[i + 1],
            second_selling[i + 1]
        )

    max_profit = 0
    for i in range(len(arr) - 1):
        max_profit = max(max_profit, second_selling_suffix_max[i] - arr[i])
    return max_profit


def solve(arr):
    single_selling_max = single_selling(arr)
    double_selling_max = double_selling(arr)
    return max(single_selling_max, double_selling_max)


# A = [3, 3, 5, 0, 0, 3, 1, 4]      # 6
# A = [1, 2, 3, 4, 5]               # 4
# A = [7, 6, 4, 3, 1]               # 0
# A = [2, 1, 4, 5, 2, 9, 7]         # 11
A = [2, 1, 2, 0, 1]               # 2
print(solve(A))
