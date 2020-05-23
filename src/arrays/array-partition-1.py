def solve(arr):
    arr.sort()

    s = 0
    for i in range(0, len(arr), 2):
        s += arr[i]

    return s
