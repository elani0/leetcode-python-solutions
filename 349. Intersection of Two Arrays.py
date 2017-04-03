# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 20:55:05 2016

@author: Elani
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter_set = set(nums1) & set(nums2)
        return list(inter_set)
        
if __name__ =="__main__":
    s=Solution()
    nums1=[1,2,2,1]
    nums2=[2,2]
    re=s.intersection(nums1,nums2) 
    for i in re :
        print i 