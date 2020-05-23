from collections import defaultdict


def solve(arr, k):
    s = 0
    prefix = []
    for elem in arr:
        s += elem
        prefix.append(s)

    count = 0
    previous_s = defaultdict(lambda: 0)

    for elem in prefix:
        if elem == k:
            count += 1

        count += previous_s[elem - k]
        previous_s[elem] += 1

    return count


A = [1, 1, 1]
B = 2
print(solve(A, B))
