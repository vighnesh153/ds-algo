def solve(arr):
    count1 = count2 = 0
    first = second = None

    for elem in arr:
        if first == elem:
            count1 += 1
        elif second == elem:
            count2 += 1
        elif count1 == 0:
            count1 = 1
            first = elem
        elif count2 == 0:
            count2 = 1
            second = elem
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0
    for elem in arr:
        count1 += 1 if elem == first else 0
        count2 += 1 if elem == second else 0

    result = []
    if count1 > len(arr) / 3:
        result.append(first)
    if count2 > len(arr) / 3:
        result.append(second)

    return result


A = [1, 1, 1, 3, 3, 2, 2, 2]
print(solve(A))
