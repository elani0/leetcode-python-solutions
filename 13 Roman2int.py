# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:17:51 2017

@author: Elani
"""
#13. Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        int_sum = 0  

        for i in xrange(1,len(s)):
            if chars[s[i-1]] < chars[s[i]]:
                int_sum += -chars[s[i-1]]
            else:
                int_sum += chars[s[i-1]]
        int_sum += chars[s[-1]] 
        return int_sum