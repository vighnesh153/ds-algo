def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def solve(arr):
    last_index = len(arr) - 1
    while last_index >= 1 and arr[last_index] <= arr[last_index - 1]:
        last_index -= 1

    if last_index == 0:
        return arr[::-1]

    pivot_element_index = last_index - 1

    index = len(arr) - 1
    while True:
        if arr[index] <= arr[pivot_element_index]:
            index -= 1
        else:
            break

    arr[index], arr[pivot_element_index] = \
        arr[pivot_element_index], arr[index]

    return reverse(arr, last_index, len(arr) - 1)


res = solve([3, 2, 1])
print(res)
