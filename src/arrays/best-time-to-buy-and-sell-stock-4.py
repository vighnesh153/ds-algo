def solve(prices, k):
    if k >= len(prices) // 2:
        t_i_k_0 = 0
        t_i_k_1 = -float('inf')

        for price in prices:
            t_i_k_0 = max(t_i_k_0, t_i_k_1 + price)
            t_i_k_1 = max(t_i_k_1, t_i_k_0 - price)

        return t_i_k_0

    t_i_k_0 = [0] * (k + 1)
    t_i_k_1 = [-float('inf')] * (k + 1)

    for price in prices:
        for j in range(k, 0, -1):
            t_i_k_0[j] = max(t_i_k_0[j], t_i_k_1[j] + price)
            t_i_k_1[j] = max(t_i_k_1[j], t_i_k_0[j - 1] - price)

    return t_i_k_0[k]


A = [3, 2, 6, 5, 0, 3]
B = 2
print(solve(A, B))
