# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:52:22 2017

@author: Elani
"""
#58. Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        words = s.split()
        if len(words)==0:
            return 0
        else:
            return len(words[-1])
        