def solve(arr):
    visited = set()
    exists = set(arr)

    longest_length = 0
    for num in arr:
        if num in visited:
            continue
        visited.add(num)
        local_length = 1
        while True:
            if num + local_length in exists:
                visited.add(num + local_length)
                local_length += 1
            else:
                break
        longest_length = max(longest_length, local_length)

    return longest_length
