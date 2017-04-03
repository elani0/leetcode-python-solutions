# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 15:47:41 2017

@author: Elani
"""
#118. Pascal's Triangle

class Solution(object):
    def generate(self, numRows):

        #:type numRows: int
        #:rtype: List[List[int]]
       
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            res=[[1]]
            for i in xrange(1,numRows):
                if i == 1:
                    row_i = [1,1]
                else:
                    row_i =[1]
                    for j in xrange(1,len(res[i-1])):
                        row_i.append(res[i-1][j]+res[i-1][j-1])
                    row_i.append(1)
                    
                res.append(row_i)                 
        return res
"""
Another solution:
resultset = [[1]* (i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,  i):
            resultset[i][j] = resultset[i-1][j-1] + resultset[i-1][j]

    return resultset
"""

s = Solution()

print 'hh'
print s.generate(5)   