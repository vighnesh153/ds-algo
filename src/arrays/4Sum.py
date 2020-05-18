from typing import List


def solve(arr: List[int], target: int):
    duplex_sums = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            duplex_sums.append([arr[i] + arr[j], i, j])
    duplex_sums.sort(key=lambda x: x[0])

    duplex_dict = dict()
    for s, i, j in duplex_sums:
        duplex_dict[s] = duplex_dict.get(s, set())
        duplex_dict[s].add(tuple(sorted([i, j])))

    solutions = set()
    for key in sorted(duplex_dict.keys()):
        index_pairs = duplex_dict[key]
        matching = duplex_dict.get(target - key, set())
        for i1, j1 in index_pairs:
            for i2, j2 in matching:
                ans = [arr[i1], arr[i2], arr[j1], arr[j2]]
                if len({i1, i2, j1, j2}) == 4:
                    ans.sort()
                    solutions.add(tuple(ans))

    return [list(item) for item in solutions]


A = [0, 1, 5, 0, 1, 5, 5, -4]
B = 11
for solution in solve(A, B):
    print(solution)
