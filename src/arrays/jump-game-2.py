def solve(arr):
    last_step = len(arr) - 1

    current_index = 0
    jumps = 0
    while current_index != last_step:
        if arr[current_index] + current_index >= last_step:
            jumps += 1
            break
        max_reach = 0
        max_reach_index = None
        for i in range(1, arr[current_index] + 1):
            if arr[current_index + i] + current_index + i > max_reach:
                max_reach = arr[current_index + i] + current_index + i
                max_reach_index = current_index + i
        current_index = max_reach_index
        jumps += 1

    return jumps


A = [2, 3, 1, 1, 4]
print(solve(A))
