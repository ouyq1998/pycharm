# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm 
@File    ：15.py
@IDE     ：PyCharm 
@Author  ：ouyangqun
@Date    ：2023/8/15 16:08 
'''

class Solution(object):
    def threeSum(self, nums):
        # // Sort arrays from large to small
        orderNums = sorted(nums)
        res =  []
        for i in range(len(orderNums)):
            if orderNums[i]>0:
                break
            if i>0 and orderNums[i]==orderNums[i-1]:
                continue
            j = i+1
            k = len(orderNums)-1
            while(j<k):
                tempRes = orderNums[i]+orderNums[j]+orderNums[k]
                if(tempRes>0):
                    k=k-1
                elif(tempRes<0):
                    j= j+1
                elif(tempRes==0):
                    while (j < k and  orderNums[j] == orderNums[j+ 1]):
                        j=j+1
                    while (j < k and  orderNums[k] == orderNums[k- 1]):
                        k=k-1
                    res.append([orderNums[i],orderNums[j],orderNums[k]])
                    j = j+1
                    k = k-1

        return res


nums = [1,-1,-1,0]
s = Solution()
print(s.threeSum(nums))