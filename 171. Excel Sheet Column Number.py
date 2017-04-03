# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:24:35 2016

@author: Elani
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        list_s=list(s)
        for i in xrange(len(list_s)):
            count+=26 **i*(ord(list_s[-(i+1)])-64) 
        return count
if __name__ =="__main__":
    s=Solution()
    print s.titleToNumber('AB')