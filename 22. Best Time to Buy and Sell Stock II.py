# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 15:23:45 2017

@author: Elani

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        accumu_profit = 0
        single_profit = 0
        for i in xrange(1,len(prices)):
            if prices[i] > prices[i-1]:
                single_profit += prices[i]-prices[i-1]
            elif prices[i] < prices[i-1]:
                if single_profit>0:
                    accumu_profit += single_profit
                single_profit = 0
        if single_profit != 0:
            accumu_profit += single_profit
        return accumu_profit
              
"""
V2
#simple enough silution!
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
"""    

"""
int total = 0;
    for (int i=0; i< prices.length-1; i++) {
        if (prices[i+1]>prices[i]) total += prices[i+1]-prices[i];
    }
    
    return total;
"""            
s=Solution()
l=[1,2]
print s.maxProfit(l)                

                