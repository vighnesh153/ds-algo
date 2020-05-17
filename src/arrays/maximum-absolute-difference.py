def solve(arr):
    increment = [elem + i for i, elem in enumerate(arr)]
    decrement = [elem - i for i, elem in enumerate(arr)]

    diff1 = max(increment) - min(increment)
    diff2 = max(decrement) - min(decrement)

    return max(diff1, diff2)
