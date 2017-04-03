# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:11:14 2017

@author: Elani
"""

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None :
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        sum -= root.val
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)