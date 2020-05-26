def solve(arr1, arr2):
    dp = [[0] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]

    for i in range(1, len(arr1) + 1):
        for j in range(1, len(arr2) + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

    return max(max(row) for row in dp)


A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]
print(solve(A, B))
