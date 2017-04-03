# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 19:05:36 2017

@author: Elani
"""

#136. Single Number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        s=nums[0]
        for i in xrange(1,len(nums)):
            s = s^nums[i]
        return s
        
s=Solution()
l=[-1,-1,-2]
print s.singleNumber(l)