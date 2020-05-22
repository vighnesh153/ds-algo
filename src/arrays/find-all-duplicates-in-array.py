def solve(arr):
    for i in range(len(arr)):
        arr[i] -= 1

    n = len(arr)
    for elem in arr:
        count = arr[elem % n] // n + 1
        arr[elem % n] = n * count + arr[elem % n] % n

    result = []
    for i, elem in enumerate(arr):
        if elem // n == 2:
            result.append(i + 1)

    return result


A = [4, 3, 2, 7, 8, 2, 3, 1]
print(solve(A))
