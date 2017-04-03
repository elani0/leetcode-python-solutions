# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 09:38:44 2017

@author: Elani
"""

class Solution(object):
    def minDepth(self, node):
        """
        :type root: TreeNode
        :rtype: int
        :isRoot:int
        """
        if not node:
            return 0
        l=[]
        

        if node.left:
                l.append(self.minDepth(node.left))
        if node.right:
                l.append(self.minDepth(node.right))
        if len(l) == 0:
            return 1
        else:
            return 1+min(l)
            
   

"""
# StefanPochmann's solution
def minDepth(self, root):
    if not root: return 0
    d = map(self.minDepth, (root.left, root.right))
    return 1 + (min(d) or max(d))
    
# solution --java
    public int minDepth(TreeNode root) {
    if(root == null) return 0;
    if(root.left == null || root.right == null) {
        return 1 + Math.max(minDepth(root.left), minDepth(root.right));
    }
    return 1 + Math.min(minDepth(root.left), minDepth(root.right));
}

    
# solution 3
    def minDepth(self, root):
        if not root: 
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if (left == 0 or right == 0):
            return 1+max(left,right)
        else:
            return 1+min(left,right)
"""        