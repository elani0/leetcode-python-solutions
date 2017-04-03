# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 17:23:37 2017

@author: Elani
"""

#125. Valid Palindrome

import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        del_c = string.punctuation
        res = filter(lambda x:x not in del_c,s)
        res = res.split()
        chars=''.join(char for char in res).lower()
        print chars
        for i in xrange(len(chars)):
            if chars[i] != chars[-i-1]:
                print chars[i],chars[-i-1]
                return False
        return True
        
solu=Solution()
s="A man, a plan, a canal: Panama"
print solu.isPalindrome(s)