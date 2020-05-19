def get_just_smaller(arr):
    just_smaller_array = [-1] * len(arr)

    stack = []
    for i in range(len(arr) - 1, -1, -1):
        elem = arr[i]
        while len(stack) > 0 and elem < arr[stack[-1]]:
            index = stack.pop()
            just_smaller_array[index] = i
        stack.append(i)

    return just_smaller_array


def solve(arr):
    if len(arr) == 0:
        return 0

    just_small_left = get_just_smaller(arr)
    just_small_right = get_just_smaller(arr[::-1])[::-1]
    just_small_right = [len(arr) - i - 1 if i != -1 else len(arr) for i in just_small_right]

    max_area = -float('inf')

    for i, elem in enumerate(arr):
        left_index = just_small_left[i]
        right_index = just_small_right[i]

        width = right_index - left_index - 1
        max_area = max(max_area, width * elem)

    return max_area


A = [2, 1, 5, 6, 2, 3]
print(solve(A))
