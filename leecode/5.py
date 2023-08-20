# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm 
@File    ：5.py
@IDE     ：PyCharm 
@Author  ：ouyangqun
@Date    ：2023/8/19 18:02 
'''

class Solution(object):
    def isHW(self,s):
        if len(s)==1:
            return True
        left = 0
        right = len(s)-1
        while (left < right):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    def longestPalindrome(self, s):
        if len(s) < 1:
            return
        if len(s) == 1:
            return s
        max_length = 0
        res = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if self.isHW(s[i:j+1]):
                    if max_length < j-i+1:
                        max_length = max(max_length,j-i)
                        res = s[i:j+1]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"))






