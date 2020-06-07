# https://www.codechef.com/JUNE20B/submit/EOEO


def solve():
    for _ in range(int(input())):
        tom = int(input())
        tom_copy = tom
        k = 0
        while tom_copy % 2 == 0:
            k += 1
            tom_copy //= 2

        minimum = 1 << (k + 1)
        print(tom // minimum)


solve()
