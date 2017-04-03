# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 10:18:40 2017

@author: Elani
"""

#108. Convert Sorted Array to Binary Search Tree
"""
Description:
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums :
            return None
     
        mid = len(nums)/2
        root = TreeNode(nums[mid])
        #if len(nums[:mid]) >0:
        root.left = self.sortedArrayToBST(nums[:mid])
        #if len(nums[:mid]) >0:
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
        