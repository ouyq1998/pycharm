# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm 
@File    ：bubbleSort.py
@IDE     ：PyCharm 
@Author  ：ouyangqun
@Date    ：2023/8/22 8:53 
'''


# 不额外记录长度或者其他的信息
class ListNode():
    def __init__(self, var):
        self.var = var
        self.next = None


def bubbleSortList(nums: list):
    for i in range(len(nums)):
        for j in range(0, len(nums) - i):
            if j > 0 and j < len(nums):
                if nums[j - 1] > nums[j]:
                    temp = nums[j - 1]
                    nums[j - 1] = nums[j]
                    nums[j] = temp


# 通过数组来建立链表
def bulidLinkedlist(nums: list):
    if len(nums) < 1:
        return None
    if len(nums) == 1:
        return ListNode(nums[0])
    head = ListNode(nums[0])
    curr = head
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next
    return head


# 打印链表
def printLinkedList(head: ListNode):
    curr = head
    while (curr != None):
        print(curr.var, end=' ')
        curr = curr.next


# 获取链表的长度
def getLength(head: ListNode):
    count = 0
    curr = head
    while (curr != None):
        count += 1
        curr = curr.next
    return count


# 快排的三种方法，默认升序
# （1） 直接交换值，相对简单
# （2） 额外维护两个链表，用于存放大于基点的节点和小于基点的基点 最后链接
# （3） 不直接交换值，不使用额外链表空间，原地交换节点。较为复杂

# 方法一、直接交换值
def sortLinkedList(head: ListNode):
    curr = head.next
    pre = head
    while (curr != None):
        if pre.var > curr.var:
            temp = pre.var
            pre.var = curr.var
            curr.var = temp
        pre = curr
        curr = curr.next


def bubbleSortLinklist1(head: ListNode):
    length = getLength(head)
    for i in range(length):
        sortLinkedList(head)


# （2） 额外维护两个链表，用于存放大于基点的节点和小于基点的基点 最后链接
# 插入一个节点的数据，保持有序
def insertLinkedList(head: ListNode, val: int):
    if head == None:
        return ListNode(val)
    if val <= head.var:
        node = ListNode(val)
        node.next = head
        return node
    else:
        curr = head
        while curr.next != None:
            if curr.next.var >= val:
                node = ListNode(val)
                temp = curr.next
                curr.next = node
                node.next = temp
                return head
            curr = curr.next
        curr.next = ListNode(val)
        return head


def bubbleSortLinklist2(head: ListNode):
    if head==None:
        return
    left = None
    leftTail = None
    mid = None
    midTail = None
    right = None
    rightTail = None
    curr = head
    target = head.var
    while curr!=None:
        if curr.var==target:
            mid = insertLinkedList(mid,curr.var)
        if curr.var>target:
            right = insertLinkedList(right,curr.var)
        if curr.var<target:
            left = insertLinkedList(left,curr.var)
        curr = curr.next
    curr = left
    while curr!=None and curr.next!=None:
        curr= curr.next
    leftTail = curr

    curr = mid
    while curr != None and curr.next != None:
        curr = curr.next
    midTail = curr



    newHead  = None
    if left!=None:
        newHead = left
        leftTail.next = mid
        midTail.next = right

    return newHead




# （3） 不直接交换值，不使用额外链表空间，原地交换节点。较为复杂
def bubbleSortLinklist3(head: ListNode):
    curr = head.next
    pre = head
    while (curr != None):
        if pre.var > curr.var:
            temp = pre
            pre.next = curr.next
            curr.next = temp
            curr = pre.next
        else:
            curr = curr.next
            pre = pre.next


if __name__ == '__main__':
    a = [6,6,6,6,6,6,6,6, 5, 4, 3, 2, 1]
    head = bulidLinkedlist(a)
    printLinkedList(head)
    bubbleSortLinklist2(head)
    # head = insertLinkedList(head, 8)
    print()
    printLinkedList(head)
