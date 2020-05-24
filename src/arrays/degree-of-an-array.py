from collections import defaultdict


def solve(arr):
    first_occurrences = dict()
    last_occurrences = dict()
    counter = defaultdict(lambda: 0)
    for i, elem in enumerate(arr):
        if counter[elem] == 0:
            first_occurrences[elem] = i
        counter[elem] += 1
        last_occurrences[elem] = i
    degree = max(counter.values())
    max_values = filter(
        lambda _key: counter[_key] == degree,
        counter.keys()
    )
    min_length = len(arr)
    for key in max_values:
        index1 = first_occurrences[key]
        index2 = last_occurrences[key]
        min_length = min(min_length, index2 - index1 + 1)
    return min_length


A = [1, 2, 2, 3, 1]
print(solve(A))
