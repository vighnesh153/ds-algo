def solve(arr):
    arr.sort()

    p1 = arr[-1] * arr[-2] * arr[-3]
    p2 = arr[-1] * arr[0] * arr[1]

    return max(p1, p2)


A = [1, 2, 3, 4]
print(solve(A))
