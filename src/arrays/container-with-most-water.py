def solve(arr):
    start = 0
    end = len(arr) - 1

    max_area = -float('inf')

    while start < end:
        height = min(arr[start], arr[end])
        max_area = max(max_area, height * (end - start))

        if arr[end] > arr[start]:
            start += 1
        else:
            end -= 1

    return max_area


A = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(solve(A))
