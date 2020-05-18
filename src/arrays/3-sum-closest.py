from bisect import bisect
from typing import List


def solve(arr: List[int], target: int):
    answers = []
    arr.sort()

    for i in range(len(arr)):
        j = i + 1
        k = len(arr) - 1

        while j < k:
            s = arr[i] + arr[j] + arr[k]
            if s == target:
                return target
            elif s > target:
                k -= 1
            else:
                j += 1
            answers.append(s)

    answers.sort()
    position = bisect(answers, target)
    if position == 0:
        return answers[0]
    if position == len(answers):
        return answers[-1]

    smaller = answers[position - 1]
    bigger = answers[position]

    return smaller if target - smaller < bigger - target else bigger


A = [-1, 2, 1, -4]
B = 1
print(solve(A, B))
