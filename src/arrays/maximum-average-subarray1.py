def solve(arr, k):
    s = sum(arr[:k])
    average = s / k

    for i in range(k, len(arr)):
        s += arr[i]
        s -= arr[i - k]
        average = max(average, s / k)

    return average


inputs = [
    [1, 12, -5, -6, 50, 3],
    4
]
print(solve(*inputs))
