# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm
@File    ：912.py
@IDE     ：PyCharm
@Author  ：ouyangqun
@Date    ：2023/8/17 16:56
'''
import random


class Solution(object):

    def quick_sort(self,nums,begin,end):
        if begin >= end:  # 递归的退出条件
            return
        left = begin
        right = end
        mid = nums[begin]
        while left < right:
            while left<right and nums[right]>= mid:
                right-=1
            nums[left] = nums[right]
            while left<right and nums[left] <= mid:
                left+=1
            nums[right] = nums[left]
        nums[left] = mid
        # quick sort left
        self.quick_sort(nums,0,left-1)
        # quick sort right
        self.quick_sort(nums,right+1,end)
        return nums



    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

s= Solution()
nums =[0,5,9,4,69,2,659,2,65,52,2,6,2,5,62,56255,5,32,1,8]
s.sortArray(nums)
print(nums)