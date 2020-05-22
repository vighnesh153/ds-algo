def solve(arr):
    output = []
    p = 1
    for elem in arr:
        output.append(p)
        p *= elem

    p = 1
    for i in range(len(arr) - 1, -1, -1):
        output[i] *= p
        p *= arr[i]

    return output


A = [1, 2, 3, 4]
print(solve(A))
