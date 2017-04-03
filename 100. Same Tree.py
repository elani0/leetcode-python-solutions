# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:09:30 2016

@author: Elani
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == q and q == None:
            return True
        #this if is needed,in case of one of p ,q is None
        if p ==None or q== None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left,q.left) & self.isSameTree(p.right,q.right)
        else:
            return False