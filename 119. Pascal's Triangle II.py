# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 17:19:17 2017

@author: Elani
#The first Ac problem :)
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l=[1]
        for i in xrange(rowIndex):
            l.insert(0,0)
            l.append(0)
            for j in xrange(len(l)-1):
                l[j] = l[j]+l[j+1]
            l.pop()
        return l