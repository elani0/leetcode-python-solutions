# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 16:31:21 2017

@author: Elani
"""

#198. House Robber
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)<= 2:
            return max(nums)
        money = [nums[0]]
        money.append(max(nums[:2]))
        for i in xrange(2,len(nums)):
            money.append(max(money[i-2]+nums[i],money[i-1]))
        return money[-1]
        
        
'''
class Solution:
    
    def rob(self, nums):
        
        last, now = 0, 0
        
        for i in nums: last, now = now, max(last + i, now)
                
        return now
'''