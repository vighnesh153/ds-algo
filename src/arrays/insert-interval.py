def solve(intervals, new_interval):
    intervals.append(new_interval)
    intervals.sort(reverse=True)

    result = []
    while len(intervals) > 0:
        if len(result) == 0:
            result.append(intervals.pop())
        else:
            prev_interval = result.pop()
            next_interval = intervals.pop()
            if next_interval[0] <= prev_interval[1]:
                result.append([
                    prev_interval[0],
                    max(prev_interval[1], next_interval[1])
                ])
            else:
                result.append(prev_interval)
                result.append(next_interval)

    return result


A = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
B = [4, 8]
print(solve(A, B))
