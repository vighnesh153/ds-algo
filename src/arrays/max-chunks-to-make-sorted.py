def solve(arr):
    prefix_max = []
    max_till_now = -float('inf')
    for elem in arr:
        max_till_now = max(max_till_now, elem)
        prefix_max.append(max_till_now)

    chunks = 0
    minimum = arr[-1]
    for i in range(len(arr) - 1, -1, -1):
        if i > 0:
            minimum = min(minimum, arr[i])
            if prefix_max[i - 1] <= minimum:
                chunks += 1
                minimum = arr[i - 1]
        else:
            chunks += 1

    return chunks


A = [2, 0, 1, 2]
print(solve(A))
