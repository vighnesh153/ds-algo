def solve(arr):
    visited = set()
    max_length = 0

    for elem in arr:
        if elem not in visited:
            length = 1
            current = elem
            while current not in visited:
                visited.add(current)
                current = arr[current]
                length += 1
            max_length = max(max_length, length - 1)

    return max_length


A = [5, 4, 0, 3, 1, 6, 2]
print(solve(A))
