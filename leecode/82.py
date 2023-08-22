# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm 
@File    ：82.py
@IDE     ：PyCharm 
@Author  ：ouyangqun
@Date    ：2023/8/21 18:01 
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def buildTree(self,list):
        if len(list)==0:
            return
        head = ListNode(list[0])
        curr = head
        for i in range(1,len(list)):
            curr.next= ListNode(list[i])
            curr = curr.next
        curr.next = ListNode(list[-1])
        return head
    def printTree(self,head:ListNode):
        curr = head
        while(curr.next!=None):
            print(curr.val)
            curr=curr.next

    def deleteDuplicates(self, head:ListNode):
        tempSet= set()
        curr = head
        pre = None
        while(curr.next!=None):
            if  curr.val not in tempSet:
                pre = curr
                tempSet.add(curr.val)
                curr = curr.next
            else:
                curr = curr.next
                pre.next = curr
        return head


if __name__ == '__main__':
    s = Solution()
    head = s.buildTree([1,2,3,3,4,4,5])
    s.printTree(head)
    s.deleteDuplicates(head)
    s.printTree(head)

