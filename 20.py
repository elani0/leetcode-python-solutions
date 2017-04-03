# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:32:25 2017

@author: Elani
"""
#20. Valid Parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        pre = ['(','{','[']
        suf = {')':0,'}':1,']':2}
        
        for ix in xrange(len(s)):
            if s[ix] in pre:
                l.append(s[ix])
            elif s[ix] in suf:
                if len(l) == 0 or (len(l)>0 and l[-1] != pre[suf[s[ix]]]):
                    return False
                else:
                    l.pop()

        if len(l)==0:
            return True
        else:
            return False
            
#dict = {"]":"[", "}":"{", ")":"("}
#thats wonderful!