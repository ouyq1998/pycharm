# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm 
@File    ：46.py
@IDE     ：PyCharm 
@Author  ：ouyangqun
@Date    ：2023/8/19 18:33 
'''


class Solution(object):

    def __init__(self):
        self.res = []
        self.path = []

    def backtracking(self, nums, used):
        if len(nums) == len(self.path):
            self.res.append(self.path[:])
            return
        if len(nums) < len(self.path):
            return
        for i in range(len(nums)):
            if used[i] == 1:
                continue
            self.path.append(nums[i])
            used[i] = 1
            self.backtracking(nums, used)
            used[i] = 0
            self.path.pop()

    def permute(self, nums):
        self.backtracking(nums, [0 for _ in range(len(nums))])
        return self.res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
