from collections import defaultdict


def solve(arr, k):
    duplicates = defaultdict(list)
    elements = set()

    for i, elem in enumerate(arr):
        duplicates[elem].append(i)
        elements.add(elem)

    for elem in elements:
        indices = duplicates[elem]
        for i in range(1, len(indices)):
            if indices[i] - indices[i - 1] <= k:
                return True

    return False


A = [1, 2, 3, 1, 2, 3]
print(solve(A, 2))
