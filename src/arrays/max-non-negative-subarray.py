class SubArr:
    def __init__(self, arr, i, j):
        self.sum = sum(arr[ind] for ind in range(i, j + 1))
        self.index = i
        self.length = j - i + 1

    def __lt__(self, other):
        if self.sum != other.sum:
            return self.sum > other.sum

        if self.length != other.length:
            return self.length > other.length

        return self.index < other.index


def solve(arr):
    start = None
    end = None

    result = []
    for i, elem in enumerate(arr):
        if elem >= 0:
            if start is None:
                start = end = i
            else:
                end = i
        else:
            if start is not None:
                result.append(SubArr(arr, start, end))
            start = None
            end = None

    if start is not None:
        result.append(SubArr(arr, start, end))

    if len(result) == 0:
        return []

    result.sort()
    s_index = result[0].index
    s_len = result[0].length
    return arr[s_index:s_index + s_len]


res = solve([10, -1, 2, 3, -4, 100])
print(res)
