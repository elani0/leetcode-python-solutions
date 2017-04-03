# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 20:48:49 2017

@author: Elani
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in xrange(l-1):
            for j in xrange(i+1,l,1):
                if nums[i]+nums[j] == target:
                    return [i,j]

target = 6
nums=[3,2,4]

solution=Solution();
print solution.twoSum(nums,target)