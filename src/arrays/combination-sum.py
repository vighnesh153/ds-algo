def recursion(arr, target, index, solutions, current):
    if target == 0:
        solutions.append(current[:])
        return

    if target < 0 or index >= len(arr):
        return

    recursion(arr, target - arr[index], index, solutions, current + [arr[index]])
    recursion(arr, target, index + 1, solutions, current)


def solve(arr, target):
    arr = list(set(arr))
    arr.sort()
    while len(arr) > 0 and arr[-1] > target:
        arr.pop()

    solutions = []
    recursion(arr, target, 0, solutions, [])
    return solutions


A = [2, 3, 5]
B = 8
print(solve(A, B))
