# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:33:57 2016

@author: Elani
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele=0
        ele_count=0
        for i in set(nums):
            if nums.count(i) >= len(nums)/2 and nums.count(i) >ele_count:
                ele=i
                ele_count=nums.count(i)
        return ele
                
            
if __name__ == "__main__":
    s=Solution()
    nums=[3,3,4]
    print s.majorityElement(nums)