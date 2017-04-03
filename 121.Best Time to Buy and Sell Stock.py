# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 11:01:53 2017

@author: Elani
"""

import numpy as np
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        #Time Limitted solution
        if not prices:
            return 0
            
        max_pro = 0
        ix = -1
        for i in xrange(1,len(prices)):
            min_before = min(prices[0:i])
            if prices[i] - min_before > max_pro:              
                max_pro = prices[i] - min_before
                ix = i+1
        if max_pro > 0:
            return max_pro
        else:
            return 0
        """
        
        #dynamic proograming
        if not prices:
            return 0
        accumu_pro = []
        for i,p in enumerate(prices):
            if i == 0:
                accumu_pro.append(0)
            else:
                #today's price - yesterday's price + accumulate_profit
                accumu_pro.append(max(0, p - prices[i-1] + accumu_pro[-1]))
        print accumu_pro      
        return max(accumu_pro)
            
s=Solution()
print s.maxProfit([7,1,5,3,6,4])