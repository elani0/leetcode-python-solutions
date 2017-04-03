# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#101. Symmetric Tree
import os
import os.path
import numpy as np

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isEqual(self,t1,t2):
        if not t1 and not t2:
            return True
        elif t1 and t2:
            if t1.val!=t2.val:
                return False
            else :
                return self.isEqual(t1.left,t2.right) and self.isEqual(t1.right,t2.left)
        else:
            return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isEqual(root.left,root.right)
            
"""            
#iteratively
def isSymmetric(self, root):
      if root is None:
          return True
      stack = [(root.left, root.right)]
      while stack:
          left, right = stack.pop()
          if left is None and right is None:
              continue
          if left is None or right is None:
              return False
          if left.val == right.val:
              stack.append((left.left, right.right))
              stack.append((left.right, right.left))
          else:
              return False
      return True
"""