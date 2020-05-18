def solve(arr: [int]):
    iterator = 1
    modifier = 1

    while iterator < len(arr):
        if arr[iterator] != arr[iterator - 1]:
            arr[modifier] = arr[iterator]
            modifier += 1
        iterator += 1

    return modifier


# It doesn't matter what values are set beyond the
# unique length because we can just pop them out
A = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solve(A))
print(A)
