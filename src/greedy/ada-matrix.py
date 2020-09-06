# https://www.codechef.com/SEPT20B/problems/ADAMAT

for _ in "." * int(input()):
    n = int(input())
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    ops = 0
    for r in range(n - 1, -1, -1):
        if ops % 2 == 0 and matrix[r][0] == n * r + 1:
            continue
        elif ops % 2 == 1 and matrix[0][r] == n * r + 1:
            continue
        ops += 1

    print(ops)
