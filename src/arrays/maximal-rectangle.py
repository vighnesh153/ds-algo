def get_just_smaller(arr):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        elem = arr[i]
        while len(stack) > 0 and elem < arr[stack[-1]]:
            index = stack.pop()
            result[index] = i
        stack.append(i)

    return result


def get_max_histogram_area(arr):
    just_smaller_left = get_just_smaller(arr)
    just_smaller_right = [len(arr) - i - 1 if i != -1 else len(arr) for i in get_just_smaller(arr[::-1])[::-1]]

    max_area = 0
    for i, elem in enumerate(arr):
        left_index = just_smaller_left[i]
        right_index = just_smaller_right[i]

        width = right_index - left_index - 1
        max_area = max(max_area, width * elem)

    return max_area


def solve(arr):
    for i, row in enumerate(arr):
        arr[i] = list(map(int, row))

    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                continue
            arr[i][j] += arr[i - 1][j]

    max_area = 0
    for row in arr:
        max_area = max(max_area, get_max_histogram_area(row))

    return max_area


A = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(solve(A))
