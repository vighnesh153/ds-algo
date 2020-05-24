def get_max_sums(arr, k):
    prefix_max = []
    prefix_max_indices = []
    _curr_max = -float('inf')
    index = -1
    for i, elem in enumerate(arr):
        if elem > _curr_max:
            _curr_max = elem
            index = i
        prefix_max.append(_curr_max)
        prefix_max_indices.append(index)

    suffix_max = [-1 for _ in arr]
    suffix_max_indices = [-1 for _ in arr]
    _curr_max = -float('inf')
    index = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= _curr_max:
            _curr_max = arr[i]
            index = i
        suffix_max[i] = _curr_max
        suffix_max_indices[i] = index

    s = 0
    indices = []
    for j in range(len(arr)):
        if j - k < 0:
            continue
        if j + k >= len(arr):
            continue
        _sum = arr[j] + prefix_max[j - k] + suffix_max[j + k]
        if _sum > s:
            s = _sum
            indices = [
                prefix_max_indices[j - k],
                j,
                suffix_max_indices[j + k]
            ]

    return s, indices


def solve(arr, k):
    s = sum(arr[:k])
    subarray_sum = [s]
    for i in range(k, len(arr)):
        s += arr[i]
        s -= arr[i - k]
        subarray_sum.append(s)

    return get_max_sums(subarray_sum, k)


A = [1, 2, 1, 2, 6, 7, 5, 1]
B = 2
print(solve(A, B))
