from collections import Counter


def recursion(counter, keys, index, solutions, current):
    if index >= len(keys):
        solutions.append(current[:])
        return

    key = keys[index]
    for i in range(counter[key] + 1):
        for _ in range(i):
            current.append(key)
        recursion(counter, keys, index + 1, solutions, current)
        for _ in range(i):
            current.pop()


def solve(arr):
    counter = Counter(arr)
    keys = list(counter.keys())
    keys.sort()
    solutions = []
    recursion(counter, keys, 0, solutions, [])
    return solutions


A = [1, 2, 2, 3]
for sol in solve(A):
    print(sol)
