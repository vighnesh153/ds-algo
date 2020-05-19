def solve(arr):
    last_index = len(arr) - 1

    current_index = 0
    while current_index <= last_index:
        if current_index + arr[current_index] >= last_index:
            return True

        max_reach = 0
        max_reach_index = None
        for i in range(1, arr[current_index] + 1):
            reach = arr[current_index + i] + current_index + i
            if reach > max_reach:
                max_reach = reach
                max_reach_index = current_index + i

        if max_reach_index is None:
            return False
        current_index = max_reach_index


A = [3, 2, 1, 0, 4]
print(solve(A))
