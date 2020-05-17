def solve(arr):
    global_max = -float('inf')
    local_max = -float('inf')

    for item in arr:
        local_max = max(local_max + item, item)
        global_max = max(global_max, local_max)

    return global_max


res = solve([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)
