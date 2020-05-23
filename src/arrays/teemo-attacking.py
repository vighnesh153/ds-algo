def solve(arr, duration):
    if len(arr) == 0:
        return 0

    result = 0
    start = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > duration:
            result += arr[i - 1] + duration - start
            start = arr[i]

    result += arr[-1] + duration - start
    return result


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = 5
print(solve(A, B))
