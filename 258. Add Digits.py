# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:50:42 2016

@author: Elani
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=str(num)
        while len(s)>1:
            chars=list(s)
            numbers=[int(i) for i in chars]
            sum_s=sum(numbers)
            s=str(sum_s)
        return int(s)