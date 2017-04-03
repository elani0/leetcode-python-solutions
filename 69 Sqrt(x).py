# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:43:29 2017

@author: Elani
"""

#69. Sqrt(x)
#Implement int sqrt(int x).
#Compute and return the square root of x.
#Use Newton method.ref-wikipedia
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r=x
        while r*r>x:
            r=(r+x/r)/2
        return r