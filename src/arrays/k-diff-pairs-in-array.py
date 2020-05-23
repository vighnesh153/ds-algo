from collections import Counter


def solve(arr, k):
    if k < 0:
        return 0

    counter = Counter(arr)
    arr = set(arr)

    count = 0

    for elem in arr:
        diff = elem - k
        if diff == elem:
            count += 1 if counter[elem] > 1 else 0
        elif elem > diff:
            count += 1 if diff in arr else 0

    return count


A = [1, 3, 1, 5, 4]
B = 0
print(solve(A, B))
