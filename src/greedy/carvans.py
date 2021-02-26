# https://www.codechef.com/LRNDSA01/problems/CARVANS

for _ in range(int(input())):
    n = int(input())
    speeds = list(map(int, input().split()))

    count = 0
    min_speed = float('inf')
    for speed in speeds:
        if speed <= min_speed:
            count += 1
        min_speed = min(min_speed, speed)

    print(count)
