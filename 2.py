# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 21:37:45 2017

@author: Elani
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = 0
        l3_pre = None
        head = 1
        while not (l1 == None and l2 == None):
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
                
            s = s + l1.val + l2.val
            l3 = ListNode(0)
            l3.val = s%10
            l3.next = None
            s = s/10
 
            if head == 1:
                head = 0
                first_node = l3
            else:
                l3_pre.next = l3
            l3_pre = l3

            l1 = l1.next
            l2 = l2.next
          
        if s > 0:
            l3 = ListNode(0)
            l3.val = s
            l3_pre.next = l3
            l3.next = None
        return first_node