# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 22:02:16 2017

@author: Elani
"""

#3.Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #keys:record every char and its position.If find its twin,move forward the start pos.
 
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength