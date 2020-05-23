def solve(arr):
    global_max = 0
    local_count = 0

    for elem in arr:
        if elem == 0:
            local_count = 0
        else:
            local_count += 1
            global_max = max(global_max, local_count)

    return global_max
