def solve(intervals):
    intervals.sort(reverse=True)
    result = []

    while len(intervals) > 0:
        if len(result) == 0:
            result.append(intervals.pop())
        else:
            prev_interval = result.pop()
            next_interval = intervals.pop()

            if next_interval[0] <= prev_interval[1]:
                new_interval = [
                    prev_interval[0],
                    max(prev_interval[1], next_interval[1])
                ]
                result.append(new_interval)
            else:
                result.append(prev_interval)
                result.append(next_interval)

    return result


A = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(solve(A))
