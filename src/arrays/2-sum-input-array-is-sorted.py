def solve(arr, t):
    i = 0
    j = len(arr) - 1

    while i < j:
        s = arr[i] + arr[j]

        if s == t:
            return [i + 1, j + 1]
        elif t < s:
            j -= 1
        else:
            i += 1
