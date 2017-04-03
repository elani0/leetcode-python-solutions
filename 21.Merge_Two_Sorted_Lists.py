# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 18:21:45 2017

@author: Elani
"""
# 21.Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total_head =  total_next = None
        l1_next = l1
        l2_next = l2
        
        while(l1_next and l2_next):
            if l1_next.val < l2_next.val:
                if not total_head:
                    total_head = l1_next
                    total_next = total_head
                else:
                    total_next.next =l1_next 
                    total_next = total_next.next
                l1_next = l1_next.next
                    
            elif l1_next.val > l2_next.val:
                if not total_head:
                    total_head = l2_next
                    total_next = total_head
                else:
                    total_next.next = l2_next
                    total_next = total_next.next
                l2_next = l2_next.next
                 
            else:
                if not total_head:
                    total_head = l1_next
                    l1_next = l1_next.next
                    total_head.next = l2_next
                    total_next = l2_next
                    l2_next = l2_next.next
                else:
                    total_next.next=l1_next
                    total_next = l1_next
                    l1_next = l1_next.next
                    
                    total_next.next=l2_next
                    total_next = l2_next
                    l2_next = l2_next.next
        
        if l1_next:
            if not total_next:
                return l1_next
            else:
                total_next.next = l1_next
        elif l2_next:
            if not total_next:
                return l2_next
            else:
                total_next.next = l2_next
            
        return total_head
        
"""
# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
    
# recursively    
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
        
# in-place, iteratively        
def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

"""