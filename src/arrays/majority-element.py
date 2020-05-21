from collections import Counter


def solve(arr):
    counter = Counter(arr)

    max_count = -float('inf')
    value = None

    for key in counter.keys():
        if counter[key] > max_count:
            value = key
            max_count = counter[key]

    return value
