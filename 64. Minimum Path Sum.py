# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 17:02:19 2017

@author: Elani
"""
#64. Minimum Path Sum
import numpy as np
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return None
        m = len(grid)
        n = len(grid[0])
        print m,n
        path = np.zeros((m,n))
        path[0][0] = grid[0][0]
        #init the first line
        for i in xrange(1,n):
            path[0,i]=path[0,i-1]+grid[0][i]
        #init the first column
        for j in xrange(1,m):
            path[j][0] = path[j-1][0]+grid[j][0]
            
        for i in xrange(1,m):
            for j in xrange(1,n):
                path[i][j] = grid[i][j] + min(path[i][j-1] ,path[i-1][j])
                
        return path[-1][-1]
        
s=Solution()
#l=[[1,2],[3,1]]
l=[[0]]
print s.minPathSum(l)