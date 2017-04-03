# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:03:50 2016

@author: Elani
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next != None:
            node.val = node.next.val
            node.next = node.next.next
          
        