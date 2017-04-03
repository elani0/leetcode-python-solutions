# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 10:45:03 2017

@author: Elani
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def isBalancedAndCalcuDepth(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root :
            return (True,0)

        ibleft, dleft = self.isBalancedAndCalcuDepth(root.left)
        ibright, dright =  self.isBalancedAndCalcuDepth(root.right)
        
        if ibleft and ibright and abs(dleft - dright)<=1:
            return (True,1+max(dleft,dright))
        else:
            return (False,1+max(dleft,dright))
        
    def isBalanced(self, root):
        ib,depth = self.isBalancedAndCalcuDepth(root)
        return ib

#solution 2:计算深度的函数 分开定义
"""
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True

        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if not root:
            return 0

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
"""        