# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 12:33:33 2017

@author: Elani
"""

#26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)<2:
            return 1
        ix = 1
        
        for i in xrange(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[ix] = nums[i]
                ix += 1
        #print nums
        return ix
     
     
"""
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1
"""
        
s = Solution()
l=[1,2,3,3,4,5,5]
print s.removeDuplicates(l)