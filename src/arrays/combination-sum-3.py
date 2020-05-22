def recursion(n, k, s, start, current, solutions):
    if start == 10 or start > n:
        if n == s and k == 0:
            solutions.append(current[:])
        return

    current.append(start)
    recursion(n, k - 1, s + start, start + 1, current, solutions)
    current.pop()

    recursion(n, k, s, start + 1, current, solutions)


def solve(k, n):
    solutions = []
    recursion(n, k, 0, 1, [], solutions)
    return solutions


for sol in solve(3, 9):
    print(sol)
