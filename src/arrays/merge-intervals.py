class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def solve(intervals, new_interval):
    intervals.append(new_interval)
    intervals.sort(key=lambda i: [i.start, i.end], reverse=True)

    new_intervals = []
    while len(intervals) > 0:
        if len(new_intervals) == 0:
            new_intervals.append(intervals.pop())
        else:
            prev_interval = new_intervals.pop()
            next_interval = intervals.pop()

            if prev_interval.end < next_interval.start:
                new_intervals.append(prev_interval)
                new_intervals.append(next_interval)
            else:
                merged_interval = Interval()
                merged_interval.start = prev_interval.start
                merged_interval.end = max(prev_interval.end, next_interval.end)
                new_intervals.append(merged_interval)

    return [[i.start, i.end] for i in new_intervals]


res = solve([
    Interval(1, 3),
    Interval(6, 9)
], Interval(2, 5))
print(res)
