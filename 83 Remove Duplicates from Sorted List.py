# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:09:40 2017

@author: Elani
"""

#83. Remove Duplicates from Sorted List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        preV = head.val
        cur=head.next
        tail = head
        while cur!=None:
            if cur.val != preV:
                tail.next = cur
                tail = tail.next
                preV=cur.val
            cur = cur.next
        tail.next=None
        return head
"""
def deleteDuplicates(self, head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            

        return head
"""