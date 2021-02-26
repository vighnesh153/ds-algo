# https://www.codechef.com/LRNDSA01/problems/FCTRL

for _ in range(int(input())):
    n = int(input())

    count = 0
    power = 5

    while True:
        k = n // power
        if k == 0:
            break
        count += k
        power *= 5

    print(count)
