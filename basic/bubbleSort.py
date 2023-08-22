# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm 
@File    ：bubbleSort.py
@IDE     ：PyCharm 
@Author  ：ouyangqun
@Date    ：2023/8/22 8:53 
'''

class ListNode():
    def __init__(self,var):
        self.var = var
        self.next = None

def bubbleSortList(nums:list):
    for i in range(len(nums)):
        for j in range(0,len(nums)-i):
            if j>0 and j < len(nums):
                if nums[j-1]> nums[j]:
                    temp = nums[j-1]
                    nums[j-1]=nums[j]
                    nums[j]=temp

def bubbleSortLinklist(head:ListNode):
    pass

def bulidLinklist(nums:list):
    if len(nums)<1:
        return  None
    if len(nums==1):
        return ListNode(nums[0])
    head = ListNode(nums[0])
    curr = head
    for i in range(1,len(nums)):
        curr.next = ListNode(nums[i])
        curr=curr.next
    return head

if __name__ == '__main__':
    a = [6,5,4,3,2,1]
    for i in a:
        print(i)
    bubbleSortList(a)
    for i in a:
        print(i)