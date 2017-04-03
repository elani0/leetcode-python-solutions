# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:12:15 2017

@author: Elani
"""

#107. Binary Tree Level Order Traversal II
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l=[]
        if not root:
            return l
        stack = [[root]]
        l.insert(0,[root.val])
        
        while stack:
            nodes=stack.pop(0)
            lrNode=[]
            lrVal=[]
            for t in nodes:
                if t.left :
                    lrNode.append(t.left)
                    lrVal.append(t.left.val)
                    
                if t.right:
                    lrNode.append(t.right)
                    lrVal.append(t.right.val)
            if lrVal:
                stack.append(lrNode)
                l.insert(0,lrVal)
            
        return l
        