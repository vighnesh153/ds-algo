# https://www.codechef.com/LRNDSA01/problems/MULTHREE

hack = {
    2: [2, 4, 8, 6],
    4: [4, 8, 6, 2],
    8: [8, 6, 2, 4],
    6: [6, 2, 4, 8],
}

for _ in range(int(input())):
    k, d0, d1 = map(int, input().split())

    arr = [d0, d1]
    next_num = (d0 + d1) % 10
    while True:
        arr.append(next_num)
        if next_num % 2 == 0:
            break
        next_num = (next_num * 2) % 10

    is_multiple_of_3 = False

    if len(arr) >= k:
        is_multiple_of_3 = sum(arr[:k]) % 3 == 0
    else:
        prefix_sum = sum(arr[:-1])
        if arr[-1] == 0:
            is_multiple_of_3 = prefix_sum % 3 == 0
        else:
            remaining = k - len(arr) + 1
            groups = remaining // 4
            mod = remaining % 4
            s = prefix_sum + groups * (2 + 4 + 6 + 8) + sum(hack[arr[-1]][:mod])
            is_multiple_of_3 = s % 3 == 0

    print('YES' if is_multiple_of_3 else 'NO')
