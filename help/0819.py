# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm 
@File    ：0819.py
@IDE     ：PyCharm 
@Author  ：ouyangqun
@Date    ：2023/8/19 19:42 
'''

MOD = 10**9 + 7

def countWays(n, a):
    sum_a = sum(a)
    dp = [[0] * (sum_a + 1) for _ in range(2)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(sum_a + 1):
            dp[i % 2][j] = dp[(i - 1) % 2][j] * (sum_a - i + 1) % MOD
            if j >= a[i - 1]:
                dp[i % 2][j] = (dp[i % 2][j] + dp[(i - 1) % 2][j - a[i - 1]]) % MOD

    return dp[n % 2][sum_a]

n = int(input())
a = list(map(int, input().split()))
result = countWays(n, a)
print(result)

