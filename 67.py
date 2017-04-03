# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 20:52:16 2017

@author: Elani
"""

#67
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a and not b:
            return ''
        elif (not a and b) or (a and not b):
            return a or b
        
        minLen = min(len(a),len(b))
        maxLen = max(len(a),len(b))
        if len(a)<maxLen:
            a = '0'*(maxLen-minLen)+a
        else:
            b = '0'*(maxLen-minLen)+b
        print a,b   
        ad = 0
        c=[]
        for i in xrange(1,maxLen+1):
            single_sum =int(a[-i])+int(b[-i])+ad
            ad =single_sum/2
            c.insert(0,str(single_sum%2))
        if ad>0:
            c.insert(0,'1')
        str_c =''
        return str_c.join(c)
a='11'
b='1'
s=Solution()
print  s.addBinary(a,b)