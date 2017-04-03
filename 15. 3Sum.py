# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:57:11 2016

@author: Elani
"""
class Solution(object):
    def threeSum(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        #TLE
        l=set()
        length = len(nums)
        for i in xrange(length-2):
            for j in xrange(i+1,length-1):
                for k in xrange(j+1,length):
                    if nums[i]+nums[k]+nums[j] == 0:
                        #print i,j,k
                        ele=[nums[i],nums[k],nums[j]]
                        ele.sort()
                        ele = tuple(ele)
                        l.add(ele)
        ll=[list(i) for i in l]        
        return ll
        '''
        solution=[]
        num.sort()
        
        for i in range(len(num)-1):
            if i>0 and num[i]==num[i-1]:
                continue
            left=i+1
            right=len(num)-1
            while left<right:
                val=num[i]+num[left]+num[right]
                if val==0 and [num[i],num[left],num[right]] not in solution:
                    solution.append([num[i],num[left],num[right]])
                    left=left+1
                    right=right-1
                elif val<0:
                    left=left+1
                else:
                    right=right-1
        return solution
        
if __name__ =="__main__":
    s=Solution()
    S = [-1, 0, 1, 2, -1, -4]
    ll=s.threeSum(S)
'''

l=set()
nums=[-1, 0, 1, 2, -1, -4]
length = len(nums)
for i in xrange(length-2):
    for j in xrange(i+1,length-1):
        for k in xrange(j+1,length):
            if nums[i]+nums[k]+nums[j] == 0:
                #print i,j,k
                ele=[nums[i],nums[k],nums[j]]
                ele.sort()
                ele = tuple(ele)
                l.add(ele)
ll=list(l)
'''