def solve(arr: [int], target: int):
    iterator = 0
    modifier = 0

    while iterator < len(arr):
        if arr[iterator] != target:
            arr[modifier] = arr[iterator]
            modifier += 1
        iterator += 1

    return modifier


A = [0, 1, 2, 2, 3, 0, 4, 2]
B = 2
print(solve(A, B))
print(A)
