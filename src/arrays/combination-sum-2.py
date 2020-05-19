def recursion(arr, target, index, solutions, current):
    if target == 0:
        solutions.add(tuple(current))
        return

    if target < 0 or index >= len(arr):
        return

    current.append(arr[index])
    recursion(arr, target - arr[index], index + 1, solutions, current)
    current.pop()
    recursion(arr, target, index + 1, solutions, current)


def solve(arr, target):
    solutions = set()
    arr.sort()
    recursion(arr, target, 0, solutions, [])
    return [list(item) for item in solutions]


A = [10, 1, 2, 7, 6, 1, 5]
B = 8
print(solve(A, B))
