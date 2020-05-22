# array consists of numbers from 0 to n except one of these.
def solve(arr):
    xor = 0
    for elem in arr:
        xor ^= elem

    for i in range(len(arr) + 1):
        xor ^= i

    return xor


A = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(solve(A))
