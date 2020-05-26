def solve(arr):
    is_one_bit = False

    i = 0
    while i < len(arr):
        is_one_bit = arr[i] == 0
        i += 1 if is_one_bit else 2

    return is_one_bit


A = [1, 1, 1, 0]
print(solve(A))
