# https://www.codechef.com/JUNE20B/problems/XYSTR


def solve():
    for _ in range(int(input())):
        s = input()

        count = index = 0
        while index < len(s) - 1:
            if s[index] != s[index + 1]:
                count += 1
                index += 2
            else:
                index += 1

        print(count)


solve()
