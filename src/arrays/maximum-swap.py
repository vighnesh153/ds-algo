def get_max_index(arr, i, j):
    index = None
    maximum = -float('inf')
    for x in range(i, j + 1):
        if arr[x] >= maximum:
            maximum = arr[x]
            index = x
    return index


def solve(n):
    string = str(n)
    digits = list(map(int, string))

    for i in range(len(digits)):
        max_index = get_max_index(digits, i + 1, len(digits) - 1)
        if max_index is not None:
            if digits[max_index] > digits[i]:
                digits[i], digits[max_index] = \
                    digits[max_index], digits[i]
                break

    return int("".join(map(str, digits)))


A = 9973
print(solve(A))
