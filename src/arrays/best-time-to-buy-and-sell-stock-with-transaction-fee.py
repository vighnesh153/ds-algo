def solve(prices, fee):
    t_i_k_0 = 0
    t_i_k_1 = -float('inf')

    for price in prices:
        t_i_k_0 = max(t_i_k_0, t_i_k_1 + price - fee)
        t_i_k_1 = max(t_i_k_1, t_i_k_0 - price)

    return t_i_k_0


A = [1, 3, 2, 8, 4, 9]
B = 2
print(solve(A, B))
