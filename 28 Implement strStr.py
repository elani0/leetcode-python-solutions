# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:07:49 2017

@author: Elani
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """
        #Notice : empty string is substr of any string 
        if needle == "":
            return 0
        """
        needle_len = len(needle)
        for i in xrange(len(haystack)-needle_len+1):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1
        