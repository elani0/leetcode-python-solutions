# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:58:01 2016

@author: Elani
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        re=''
        for i in xrange(1,len(s)+1,1):
            re=re+s[-i]
        '''
        
        print s[::-1]
        return s[::-1]
        
        
if __name__ == "__main__":
    s1='A man'
    s2='hello'
    s=Solution()
    s.reverseString(s2)
    #s=Solution.reverseString(s2)