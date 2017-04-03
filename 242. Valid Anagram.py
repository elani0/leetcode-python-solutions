# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:09:35 2016

@author: Elani
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls=list(s)
        ls.sort()
        lt=list(t)
        lt.sort()
        re=cmp(ls,lt)
        if re == 0:
            return True
        else:
            return False
if __name__ =="__main__":
    s='anagram'
    t='nagaram'
    sol=Solution()
    print sol.isAnagram(s,t)