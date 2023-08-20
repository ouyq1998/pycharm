def countConstructWays(a):
    mod = int(1e9 + 7)
    n = len(a)
    _sum = sum(a)

    dp = [[0] * (_sum + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for pos in range(1, n + 1):
        for curSum in range(_sum + 1):
            for num in range(1, _sum + 1):
                if num != a[pos - 1] and curSum + num <= _sum:
                    dp[pos][curSum + num] += dp[pos - 1][curSum]
                    dp[pos][curSum + num] %= mod

    return dp[n][_sum]


a1 = [1, 1, 3]
waysCount1 = countConstructWays(a1) % int(1e9 + 7)
print(waysCount1)  # 输出1

a2 = [1, 1, 1]
waysCount2 = countConstructWays(a2) % int(1e9 + 7)
print(waysCount2)  # 输出0
