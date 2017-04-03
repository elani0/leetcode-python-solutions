# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:55:15 2017

@author: Elani
"""
#88. Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        """
        for i in xrange(m,len(nums1)):
            del nums1[i]
        for j in xrange(n,len(nums2)):
            del nums2[i]
        
        print nums1

        print nums2
        if not n==0:
            if m==0:
                for i in nums2:
                    nums1.append(i)
            else:
                ix1=0
                for i in nums2:
                    if i<nums1[ix1]:
                        nums1.insert(ix1,i)
                        ix1 += 1
        """
   
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

nums1=[0]
nums2=[1]
m=0
n=1

s=Solution()

s.merge(nums1,m,nums2,n)
print  nums1