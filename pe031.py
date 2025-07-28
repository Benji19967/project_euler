def num_ways(n, coins):
    num_coins = len(coins) + 1
    dp = [[1] * (n + 1)] * num_coins
    dp[0] = [0] * (n + 1)

    for i, coin in enumerate(coins, 1):
        for j in range(1, n + 1):
            col_before = dp[i][j - coin] if j - coin >= 0 else 0
            dp[i][j] = dp[i - 1][j] + col_before
    return dp[len(coins)][n]


if __name__ == "__main__":
    print(num_ways(200, [1, 2, 5, 10, 20, 50, 100, 200]))
