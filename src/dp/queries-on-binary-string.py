# Scaler problem

def solve(s, queries):
    left_most = [-1] * len(s)
    index = -1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            index = i
        left_most[i] = index

    right_most = [-1] * len(s)
    index = -1
    for i in range(len(s)):
        if s[i] == '1':
            index = i
        right_most[i] = index

    ones_count = [0] * len(s)
    count = 0
    for i, ch in enumerate(s):
        if ch == '1':
            count += 1
        ones_count[i] = count

    result = []
    for left, right in queries:
        left = left_most[left - 1]
        right = right_most[right - 1]

        if -1 in (left, right) or left > right:
            result.append(0)
            continue

        total_bits = right - left + 1
        ones = ones_count[right] - (0 if left == 0 else ones_count[left - 1])
        result.append(total_bits - ones)

    return result


res = solve("101010", [
    [2, 2]
])
print(res)
