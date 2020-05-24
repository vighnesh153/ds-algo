def solve(arr):
    sorted_arr = sorted(arr)

    i = 0
    while i < len(arr) and arr[i] == sorted_arr[i]:
        i += 1

    if i == len(arr):
        return 0

    j = len(arr) - 1
    while j >= 0 and arr[j] == sorted_arr[j]:
        j -= 1

    return 0 if j < i else j - i + 1


A = [1, 2, 4, 5, 3]
print(solve(A))
