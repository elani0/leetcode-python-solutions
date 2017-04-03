# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:41:48 2016

@author: Elani
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        else:
            r_left = self.invertTree(root.left)
            r_right = self.invertTree(root.right)            
            root.left,root.right = r_right,r_left
            return root            
        