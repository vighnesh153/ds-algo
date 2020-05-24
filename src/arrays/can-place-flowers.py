def can_place(arr, i):
    if i == 0:
        return arr[0] == 0 and (len(arr) == 1 or arr[1] == 0)

    if i == len(arr) - 1:
        return arr[-1] == 0 and arr[-2] == 0

    return (arr[i - 1], arr[i], arr[i + 1]) == (0, 0, 0)


def solve(arr, n):
    i = 0
    while i < len(arr):
        if can_place(arr, i):
            arr[i] = 1
            n -= 1
        i += 1
    return n <= 0


A = [0, 0, 1, 0, 1]
B = 1
print(solve(A, B))
