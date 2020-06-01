# https://www.codechef.com/problems/CHN15A


class Input:
    @classmethod
    def integer_array(cls):
        return list(map(int, input().split()))


def solve():
    for _ in range(int(input())):
        n, k = Input.integer_array()
        count = 0
        for item in Input.integer_array():
            if (item + k) % 7 == 0:
                count += 1
        print(count)


solve()
