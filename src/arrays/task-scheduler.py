from collections import Counter


def solve(arr, n):
    values = list(Counter(arr).values())
    _max = max(values)
    max_count = values.count(_max)

    empty_part_count = _max - 1
    empty_part_length = n - (max_count - 1)

    if empty_part_length <= 0:
        return len(arr)

    empty_slots = empty_part_length * empty_part_count
    empty_slots -= len(arr) - _max * max_count

    return empty_slots + len(arr) if empty_slots >= 0 else len(arr)


A = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F", "G", "G", "H", "H", "I", "I", "J", "J", "K", "K", "L",
     "L", "M", "M", "N", "N", "O", "O", "P", "P", "Q", "Q", "R", "R", "S", "S", "T", "T", "U", "U", "V", "V", "W", "W",
     "X", "X", "Y", "Y", "Z", "Z"]
B = 2
print(solve(A, B))
