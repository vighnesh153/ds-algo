# https://www.codechef.com/JUNE20B/problems/EVENM


def solve():
    for _ in range(int(input())):
        n = int(input())
        matrix = [[0] * n for _ in range(n)]
        i = j = prev_j = 0
        number = 1
        max_ = n ** 2
        while number <= max_:
            matrix[i][j] = number
            number += 1
            j = (j + 1) % n

            if j % n == prev_j % n:
                i += 1
                if n % 2 == 0:
                    j = prev_j = (prev_j + 1) % n
                else:
                    j = 0

        for row in matrix:
            print(" ".join(map(str, row)))


solve()
