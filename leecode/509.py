# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm 
@File    ：509.py
@IDE     ：PyCharm 
@Author  ：ouyangqun
@Date    ：2023/8/20 15:01 
'''
class Solution(object):
    def fib(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        dp = [0 for _ in range(n)]
        dp[0]=1
        dp[1]=1
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.fib(4))