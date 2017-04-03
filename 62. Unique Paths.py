# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 17:16:50 2017

@author: Elani
"""
#62. Unique Paths

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m ==0 and n == 0:
            return 0
        l=[[[] for j in xrange(n)] for i in xrange(m)]
        for i in xrange(n):
            l[0][i] = 1
        for j in xrange(m):
            l[j][0] = 1
        for i in xrange(1,m):
            for j in xrange(1,n):
                l[i][j] = l[i-1][j]+l[i][j-1]
        return l[-1][-1]
        
        
        