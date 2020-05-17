def solve(arr: [int], target: int) -> [int]:
    prev_occurrences = dict()

    for i, elem in enumerate(arr):
        if prev_occurrences.get(target - elem, None) is not None:
            return [prev_occurrences.get(target - elem), i]
        prev_occurrences[elem] = i


print(solve([2, 7, 11, 15], 9))
