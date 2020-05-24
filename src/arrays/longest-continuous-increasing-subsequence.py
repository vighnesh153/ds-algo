def solve(arr):
    if len(arr) == 0:
        return 0

    global_max = 1
    local_length = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            local_length += 1
            global_max = max(global_max, local_length)
        else:
            local_length = 1

    return global_max


A = [2, 2, 2, 2, 2]
print(solve(A))
