# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm 
@File    ：70.py
@IDE     ：PyCharm 
@Author  ：ouyangqun
@Date    ：2023/8/20 15:05 
'''
class Solution(object):
    def climbStairs(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))