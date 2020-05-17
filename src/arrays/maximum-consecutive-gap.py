# In linear time
def solve(arr):
    if len(arr) < 2:
        return 0

    max_value = max(arr)
    min_value = min(arr)

    delta = (max_value - min_value) / (len(arr) - 1)

    min_bucket = [float('inf') for _ in range(len(arr) - 1)]
    max_bucket = [-float('inf') for _ in range(len(arr) - 1)]

    for i, elem in enumerate(arr):
        if elem == min_value or elem == max_value:
            continue

        bucket_index = int((elem - min_value) // delta)

        max_bucket[bucket_index] = max(max_bucket[bucket_index], elem)
        min_bucket[bucket_index] = min(min_bucket[bucket_index], elem)

    max_gap = 0
    prev_max = min_value
    for i in range(len(arr) - 1):
        if min_bucket[i] == float('inf'):
            continue
        max_gap = max(max_gap, min_bucket[i] - prev_max)
        prev_max = max_bucket[i]
    max_gap = max(max_gap, max_value - prev_max)

    return max_gap


res = solve([1, 10, 5])
print(res)
