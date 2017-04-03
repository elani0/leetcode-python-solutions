# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:08:50 2016

@author: Elani
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_zero = 0
        while 0 in nums:
            count_zero += 1
            nums.remove(0)
        zero_list = count_zero*[0]
        nums.extend(zero_list)
    
if __name__ == "__main__":
    s = Solution()
    nums = [0,1,0,3,12]
    s.moveZeroes(nums)
