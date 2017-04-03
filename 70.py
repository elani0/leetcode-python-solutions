# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:57:42 2017

@author: Elani
"""
"""
class Solution(object):
    def recur_climbStairs(self, x):
        if x == 0 or x ==1:
            return 1
        else:
            return self.recur_climbStairs(x-1)+self.recur_climbStairs(x-2)
            
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        z = self.recur_climbStairs(n)
        return z
"""
def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
        
s=Solution()
print s.climbStairs(5)