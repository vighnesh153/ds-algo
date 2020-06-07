# https://www.codechef.com/JUNE20B/problems/CHFICRM
no = 'NO'
yes = 'YES'


def solve(arr):
    coin_5 = coin_10 = 0

    for item in arr:
        if item == 5:
            coin_5 += 1
        elif item == 10:
            if coin_5 == 0:
                return no
            coin_5 -= 1
            coin_10 += 1
        else:
            if coin_10 != 0:
                coin_10 -= 1
            elif coin_5 >= 2:
                coin_5 -= 2
            else:
                return no

    return yes


for _ in range(int(input())):
    n = input()
    arr = list(map(int, input().split()))
    print(solve(arr))
