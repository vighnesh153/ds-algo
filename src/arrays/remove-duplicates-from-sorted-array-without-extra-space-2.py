def solve(arr):
    iterator = 2
    modifier = 2

    if len(arr) <= 2:
        return len(arr)

    while iterator < len(arr):
        if not(arr[iterator] == arr[modifier - 2]
               and arr[iterator] == arr[modifier - 2]):
            arr[modifier] = arr[iterator]
            modifier += 1
        iterator += 1

    return modifier


A = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(solve(A))
print(A)
