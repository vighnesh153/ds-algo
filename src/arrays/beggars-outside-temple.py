def solve(count_beggars, amount):
    beggars_katori = [0] * count_beggars

    for start, end, amt in amount:
        beggars_katori[start - 1] += amt
        if end < count_beggars:
            beggars_katori[end] -= amt

    for i in range(1, count_beggars):
        beggars_katori[i] += beggars_katori[i-1]

    return beggars_katori


res = solve(5, [[1, 2, 10], [2, 3, 20], [2, 5, 25]])
print(res)
