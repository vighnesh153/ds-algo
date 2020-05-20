# greedy solution
def solve(arr):
    total = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            total += arr[i] - arr[i - 1]
    return total


A = [1, 2, 3, 4, 5]
print(solve(A))
