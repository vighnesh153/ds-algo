def solve(arr):
    n = len(arr)

    for i, elem in enumerate(arr):
        arr[elem % n] = i * n + (arr[elem % n] % n)

    for i, old in enumerate(arr):
        arr[i] = old // n

    return arr


res = solve([2, 0, 1, 3])
print(res)
