def get_product(arr, start, end):
    if end < start:
        return -float('inf')

    product = 1
    for i in range(start, end + 1):
        product *= arr[i]
    return product


def product_maximizer(arr, start, end):
    if end < start:
        return -float('inf')

    if start == end:
        return arr[start]

    count_negatives = len([1 for i in range(start, end + 1) if arr[i] < 0])

    if count_negatives % 2 == 0:
        return get_product(arr, start, end)

    first_negative_index = None
    for i in range(start, end + 1):
        if arr[i] < 0:
            first_negative_index = i
            break

    last_negative_index = None
    for i in range(end, start - 1, -1):
        if arr[i] < 0:
            last_negative_index = i
            break

    left_product = get_product(arr, start, last_negative_index - 1)
    right_product = get_product(arr, first_negative_index + 1, end)

    return max(left_product, right_product)


def solve(arr):
    start = 0
    max_product = -float('inf')
    for i, elem in enumerate(arr):
        if elem == 0:
            max_product = max(
                max_product,
                product_maximizer(arr, start, i - 1)
            )
            start = i + 1

    if arr[-1] != 0:
        max_product = max(
            max_product,
            product_maximizer(arr, start, len(arr) - 1)
        )

    if 0 in arr:
        max_product = max(max_product, 0)
    return max_product


A = [-2]
print(solve(A))
